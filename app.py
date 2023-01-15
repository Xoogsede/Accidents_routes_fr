import streamlit as st
from py2neo import Graph
from geopy.geocoders import Nominatim
import folium
from pyvis.network import Network
from streamlit_folium import folium_static 
import pandas as pd
import matplotlib.pyplot as plt
import dict_correspondance 
import seaborn as sns




# Fonction pour convertir une adresse en coordonnées latitude/longitude

def geocode_address(address):
    geolocator = Nominatim(user_agent="geoapiExercises")
    try:
        location = geolocator.geocode(address)
        print(location.address)
        return location.latitude, location.longitude
    except:
        print("Erreur dans l'adresse")
    


# Création de Neo4jRepository object
URI = st.secrets['neo4j_uri']
AUTH = (st.secrets['neo4j_user'], st.secrets['neo4j_password'])




# with GraphDatabase.driver(URI, auth=AUTH) as driver:
#     driver.verify_connectivity()

def main():
    

    # Connexion à la base de données Neo4j
    graph = Graph(URI, auth=AUTH)

    st.title("Recherche d'accidents de la route")
    st.sidebar.title("Paramètres de recherche")

    # Saisie de l'adresse postale
    address = st.sidebar.text_input("Adresse postale", "", key="Adresse")
    dt_deb = st.sidebar.date_input("date de début",  label_visibility='visible', key="deb", value=pd.to_datetime("2018-12-31"))
    dt_fin = st.sidebar.date_input(label="date de fin", label_visibility='visible', key="fin")

    # Saisie du rayon de recherche
    radius = st.sidebar.number_input("Rayon de recherche (en mètres)", min_value=0, max_value=100000, value=1000)

    if st.button("Rechercher") and address!="":
        # Convertir l'adresse en coordonnées
        latitude, longitude = geocode_address(address)
        print(latitude, longitude)
        # Exécuter la requête Neo4j pour trouver les accidents dans un rayon autour de l'adresse
        query = f"""
        WITH point({{latitude: {latitude}, longitude: {longitude}}}) AS pac
        MATCH (a:Accident)
        WHERE a.Latitude IS NOT NULL AND a.Longitude IS NOT NULL
        WITH a, point.distance(point({{latitude: toFloat(a.Latitude), longitude: toFloat(a.Longitude)}}), pac) AS distance
        WHERE distance < {radius}
        RETURN a
        """
        
        graph_neo4j = graph.run(query)
        results = graph_neo4j.data()
        # convertir les résultats en DataFrame

        try:
            df = pd.DataFrame(results[0])
            df = df.T.reset_index(drop=True)
            for j in results[1:]:
                n=len(df)
                df1 = pd.DataFrame(j)
                df1 = df1.T.reset_index(drop=True)
                df.loc[n]= df1.iloc[0,:]
        except:
            df = pd.DataFrame()   
        
        
        

        # Afficher les résultats de la requête sous forme de graphe Neo4j
        st.subheader("Résultats de la requête")
        if results != []:
            
            # Récupération des correspondances
            type_meteo = dict_correspondance.Conditions_atm
            typologie = dict_correspondance.Type_de_collision       

            # Transformer les données : 
            df['Date'] = df['An'] + '-' + df['Mois'] + '-' + df['Jour'] + ' ' + df['Heure']
            
            df["Adresse_postale"] = df.Adresse_postale.str.replace("  ", "")

            df["Type_de_collision"] = df.Type_de_collision.astype('int')
            df["Conditions_atmosphériques"] = df.Conditions_atmosphériques.astype('int')



            for k,v in typologie.items():
                df['Type_de_collision'].replace(v, k.replace('_', " "), inplace=True)
            
            for k,v in type_meteo.items():
                df['Conditions_atmosphériques'].replace(v, k.replace('_', " "), inplace=True)
            
            print(df[["Date", "Adresse_postale", "Type_de_collision", "Conditions_atmosphériques"]])
            
            
            g = graph_neo4j.to_subgraph()
            st.write(g)
            
            st.dataframe(df[["Date", "Adresse_postale", "Type_de_collision"]], use_container_width =True)
            vis_format = results[0]
            # créer un objet de réseau pyvis
            vis_network = Network(notebook=True)
            # ajouter les données
            vis_network.add_nodes(vis_format)
            # afficher le réseau
            vis_network.show('accident.html')
            # st.graphviz_chart(figure_or_dot=results, use_container_width=True)
            # st.write("Résultats sur un graphe Neo4j:")
            # st.write(open('accident.html').read(), unsafe_allow_html=True)


            st.title("Localisation géographique")
            # Afficher les résultats sur une carte
            st.subheader("Résultats sur une carte")
            # Création de la carte
            map = folium.Map(location=[latitude, longitude], zoom_start=13)
            folium.Marker([latitude, longitude], popup=address, tooltip="<strong>"f'{address}'"</strong>", icon=folium.Icon(color='red')).add_to(map)
            # Ajouter les marqueurs pour les accidents
            for accident in results:
                lat = accident['a']['Latitude']
                lon = accident['a']['Longitude']
                folium.Marker([lat, lon]).add_to(map)

            map.save("carte.html")
            folium_static(map)            


            st.title("Statistique")
            st.subheader("Typologie d'accident")  
            st.write("Total accidents", df[["Type_de_collision"]].count().tolist()[0])

            
            

            fig = plt.figure(figsize = (10, 5))
            

            ax = sns.countplot(x = 'Type_de_collision', data = df)
            ax.set_xticklabels(ax.get_xticklabels(), rotation = 90)
            ax.set_title("Catégorie d'accident")
            ax.set_xlabel("Type d'accident")
            ax.set_ylabel("Nombre d'accident")

            st.pyplot(fig)
            


            # Conditions atmosphérique
            st.write("Conditions météo lors des accidents", df[["Conditions_atmosphériques"]].count().tolist()[0])

            
            
            

        
            fig = plt.figure(figsize = (10, 5))                     
            
            ax = sns.countplot(x = 'Conditions_atmosphériques', data = df)
            ax.set_title("Conditions atmosphériques")
            ax.set_xlabel("Conditions météo")
            ax.set_ylabel("Nombre d'accident")
            st.pyplot(fig)






    if st.button("Réinitialiser"):
        st.empty()

if __name__ == "__main__":
    main()