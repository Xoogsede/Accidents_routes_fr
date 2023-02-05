from app import *


def recherche():
    

    # Connexion à la base de données Neo4j
    graph = Graph(URI, auth=AUTH)

    st.title("Recherche d'accidents de la route")
    st.title("Paramètres de recherche")

    # Saisie de l'adresse postale
    cp = st.text_input("Code postal", "", key="cp")
    num_voie = st.text_input("N° et rue", "", key="Adresse")
    address = cp + ', '+ num_voie
    dt_deb = st.date_input("date de début",  label_visibility='visible', key="deb", value=pd.to_datetime("2018-12-31"))
    dt_fin = st.date_input(label="date de fin", label_visibility='visible', key="fin")

    # Saisie du rayon de recherche
    radius = st.slider("Rayon de recherche (en mètres)", min_value=0, max_value=1000, value=500)
   
    if st.button("Rechercher") and address!="":
        # Convertir l'adresse en coordonnées
        latitude, longitude = geocode_address(address)
        print(latitude, longitude)
        # Exécuter la requête Neo4j pour trouver les accidents dans un rayon autour de l'adresse
        query = f"""        
        WITH point({{latitude: {latitude}, longitude: {longitude}}}) AS pac
        MATCH (a:Accident), (u:Usager), (v:Vehicules)
        WHERE a.Latitude IS NOT NULL AND a.Longitude IS NOT NULL AND a.Num_Acc = u.Num_Acc AND a.Num_Acc = v.Num_Acc
        WITH a, point.distance(point({{latitude: toFloat(a.Latitude), longitude: toFloat(a.Longitude)}}), pac) AS distance, u, v
        WHERE distance < {radius}
        RETURN a, u, v, distance
        ORDER BY distance ;
        """
        
        results  = graph.run(query).to_data_frame()
        # st.write(results)

        # convertir les résultats en DataFrame et concaténation
        try:
            acc = pd.DataFrame.from_records(results["a"])
            usg = pd.DataFrame.from_records(results["u"])
            vhc = pd.DataFrame.from_records(results["v"])
            df = acc.merge(usg.merge(vhc, how='right', on='Num_Acc', suffixes=('_left', '_right')), how='right', on='Num_Acc', suffixes=('_left', '_right'))
        except:
            df = pd.DataFrame()   
        

        # Afficher les résultats de la requête sous forme de graphe Neo4j
        st.subheader("Résultats de la requête")
        if results.shape[0] > 0 :
            
            # Récupération des correspondances
            type_meteo = dic_convert(Conditions_atmosphériques)
            typologie = dic_convert(Type_de_collision)
            sexe = dic_convert(Sexe_usager)     
            cat_vh = dic_convert(Categorie_du_vehicule)
            
            # Transformer les données : 
            
            df = df.loc[:, ~df.columns.duplicated()]
            df = df.drop_duplicates()
            # df['occutc'] = df.occutc.fillna(-1)

            df['Date'] = df['An'].astype('str') + '-' + df['Mois'].astype('str') + '-' + df['Jour'].astype('str') + ' ' + df['Heure']
            df['Date'] = pd.to_datetime(df['Date'])            
            
            df["Adresse_postale"] = df.Adresse_postale.str.replace("  ", "")
            df["Type_de_collision"] = df.Type_de_collision.astype('int')
            df["Conditions_atmosphériques"] = df["Conditions_atmosphériques"].astype('int')
            df['sexe'] = df.sexe.astype('int')
            df['catv'] = df['catv'].astype('int')

            # Remplacement des codes par leur définitaion
            for k,v in typologie.items():
                df['Type_de_collision'].replace(v, k.replace('_', " "), inplace=True)
            
            for k,v in type_meteo.items():
                df['Conditions_atmosphériques'].replace(v, k.replace('_', " "), inplace=True)
            
            for k,v in sexe.items():
                df['sexe'].replace(v, k.replace('_', " "), inplace=True)
            
            for k,v in cat_vh.items():
                df['catv'].replace(v, k.replace('_', " "), inplace=True)


            # st.write(df['catv'])


            # sns.countplot(x='Type_de_collision', hue='sexe', data=df)
            # df[["Type_de_collision", "Conditions_atmosphériques"]].astype('category').value_counts()

            # print(df[["Date", "Adresse_postale", "Type_de_collision", "Conditions_atmosphériques"]])
            
            
            
            # st.dataframe(df[["Type_de_collision", "sexe"]].astype('category').value_counts(), use_container_width =True)
            # vis_format = results[0]
            # # créer un objet de réseau pyvis
            # vis_network = Network(notebook=True)
            # # ajouter les données
            # vis_network.add_nodes(vis_format)
            # # afficher le réseau
            # vis_network.show('static/accident.html')

            # st.graphviz_chart(figure_or_dot=results, use_container_width=True)
            # st.write("Résultats sur un graphe Neo4j:")
            # st.write(open('static/accident.html').read(), unsafe_allow_html=True)



            st.title("Statistique")
           
            total_accident = df[["Type_de_collision"]].count().tolist()[0]
            st.write(''' ## Total accidents : ''',total_accident)

            
            st.subheader("Typologie d'accident")  
            fig = plt.figure(figsize = (10, 5))           

            ax = sns.countplot(x = 'Type_de_collision', hue='sexe', data = df)
            ax.set_xticklabels(ax.get_xticklabels(), rotation = 90)
            ax.set_title("Catégorie d'accident")
            ax.set_xlabel("Type d'accident")
            ax.set_ylabel("Nombre d'accident")

            st.pyplot(fig)
            


            # Conditions atmosphérique
            st.subheader("Conditions météo lors des accidents")
            fig = plt.figure(figsize = (10, 5))                     
            
            ax = sns.countplot(x = 'Conditions_atmosphériques', hue='sexe', data = df)
            ax.set_xticklabels(ax.get_xticklabels(), rotation = 90)
            ax.set_title("Conditions atmosphériques")
            ax.set_xlabel("Conditions météo")
            ax.set_ylabel("Nombre d'accident")
            st.pyplot(fig)

            st.subheader("Catégories des véhicules")
            fig = plt.figure(figsize = (10, 5))                     
            
            ax = sns.countplot(x = 'catv', hue='sexe', data = df)
            ax.set_xticklabels(ax.get_xticklabels(), rotation = 90)
            ax.set_title("Catégories des véhicules impliqués")
            ax.set_xlabel("Catégories")
            ax.set_ylabel("Nombre d'accident")
            st.pyplot(fig)

            # Afficher les résultats sur une carte
            st.title("Localisation géographique")        
            # Création de la carte
            map = folium.Map(location=[latitude, longitude], zoom_start=13)
            folium.Marker([latitude, longitude], popup=address, tooltip="<strong>"f'{address}'"</strong>", 
                        icon=folium.Icon(color='red')).add_to(map)
            # Ajouter les marqueurs pour les accidents
            for _ , accident in acc[['Latitude', 'Longitude']].iterrows():
                folium.Marker([accident['Latitude'], accident['Longitude']]).add_to(map)

            map.save("static/carte.html")
            folium_static(map)            





    if st.button("Réinitialiser"):
        st.empty()


if __name__ == "__main__":
    recherche()

