from Accueil import *
# import fonctions as fc
import fonctions as fc


# Fonction pour convertir une adresse en coordonnées latitude/longitude
def geocode_address(address):
    geolocator = Nominatim(user_agent="geoapiExercises")
    try:
        location = geolocator.geocode(address)
        # print(location.address)
        return location.latitude, location.longitude
    except Exception:
        st.markdown(''' ## <font color='red'>🚨🚨 ERREUR DANS L'ADRESSE 🚨🚨</font>''', unsafe_allow_html=True)
        pass


def recherche():
    

    # Connexion à la base de données Neo4j
    graph = Graph(URI, auth=AUTH)

    st.title("Recherche d'accidents de la route")
    st.write('''
    ##### Entrez une adresse ou simplement un code postal pour voir les accidents \
    dans une zone.
    ##### Utilisez les dates de début et de fin pour rechercher dans une période de temps.
    ##### Utilisez le curseur pour définir un rayon de recherche. 
        ''')

    # Saisie de l'adresse postale
    cp = st.text_input("Code postal", "", key="cp")
    num_voie = st.text_input("N° et rue", "", key="Adresse")
    address = cp + ', '+ num_voie
    dt_deb = st.date_input("date de début",  label_visibility='visible', key="deb", value=fc.pd.to_datetime("2018-12-31"))
    dt_fin = st.date_input(label="date de fin", label_visibility='visible', key="fin")

    # Saisie du rayon de recherche
    radius = st.slider("Rayon de recherche (en mètres)", min_value=0, max_value=1000, value=500)
   
    if st.button("Rechercher") and address!="":
        # Convertir l'adresse en coordonnées
        try:
            latitude, longitude = geocode_address(address)
        except:
            latitude, longitude  = (48.8582532, 2.294287)
            st.markdown('''
            ## <font color='green'>Adresse incorrect, latitude et longitude initialisées sur la 🗼</font>''', unsafe_allow_html=True)
           
            
        # print(latitude, longitude)
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
            acc = fc.pd.DataFrame.from_records(results["a"])
            usg = fc.pd.DataFrame.from_records(results["u"])
            vhc = fc.pd.DataFrame.from_records(results["v"])
            df = acc.merge(usg.merge(vhc, how='right', on='Num_Acc', suffixes=('_left', '_right')), how='right', on='Num_Acc', suffixes=('_left', '_right'))
        except:
            df = fc.pd.DataFrame()   
        

        # Afficher les résultats de la requête sous forme de graphe Neo4j
        st.subheader("Résultats de la requête")
        if results.shape[0] > 0 :
            
           

            # Transformer les données : 
            
            df = df.loc[:, ~df.columns.duplicated()]
            df = df.drop_duplicates()
            # df['occutc'] = df.occutc.fillna(-1)

            df['Date'] = df['An'].astype('str') + '-' + df['Mois'].astype('str') + '-' + df['Jour'].astype('str') + ' ' + df['Heure']
            df.insert(0, 'Date', df.pop('Date'), allow_duplicates=False)

            # Récupération des correspondances
            df = fc.trouv_corresp(df=df, dictionnaire=dc, dc_list=dc.__dict__)


            df['Date'] = fc.pd.to_datetime(df['Date'])            
            df["Adresse_postale"] = df.Adresse_postale.str.replace("  ", "")
           


            st.title("Statistique")
           
            total_accident = df[["Type_de_collision"]].count().tolist()[0]
            st.write(''' ## Total accidents : ''',total_accident)

            
            st.subheader("Typologie d'accident")  
            fig = fc.plt.figure(figsize = (10, 5))           

            ax = fc.sns.countplot(x = 'Type_de_collision', hue='sexe', data = df)
            ax.set_xticklabels(ax.get_xticklabels(), rotation = 90)
            ax.set_title("Catégorie d'accident")
            ax.set_xlabel("Type d'accident")
            ax.set_ylabel("Nombre d'accident")

            st.pyplot(fig)
            


            # Conditions atmosphérique
            st.subheader("Conditions météo lors des accidents")
            fig = fc.plt.figure(figsize = (10, 5))                     
            
            ax = fc.sns.countplot(x = 'Conditions_atmosphériques', hue='sexe', data = df)
            ax.set_xticklabels(ax.get_xticklabels(), rotation = 90)
            ax.set_title("Conditions atmosphériques")
            ax.set_xlabel("Conditions météo")
            ax.set_ylabel("Nombre d'accident")
            st.pyplot(fig)

            st.subheader("Catégories des véhicules")
            fig = fc.plt.figure(figsize = (10, 5))                     
            
            ax = fc.sns.countplot(x = 'catv', hue='sexe', data = df)
            ax.set_xticklabels(ax.get_xticklabels(), rotation = 90)
            ax.set_title("Catégories des véhicules impliqués")
            ax.set_xlabel("Catégories")
            ax.set_ylabel("Nombre d'accident")
            st.pyplot(fig)

            # Afficher les résultats sur une carte
            st.title("Localisation géographique")        
            # Création de la carte
            map = fc.folium.Map(location=[latitude, longitude], zoom_start=13)
            fc.folium.Marker([latitude, longitude], popup=address, tooltip="<strong>"f'{address}'"</strong>", 
                        icon=fc.folium.Icon(color='red')).add_to(map)
            # Ajouter les marqueurs pour les accidents
            for _ , accident in acc[['Latitude', 'Longitude']].iterrows():
                fc.folium.Marker([accident['Latitude'], accident['Longitude']]).add_to(map)

            map.save("static/carte.html")
            fc.folium_static(map, width=fc._max_width_(80))            





    if st.button("Réinitialiser"):
        st.empty()


if __name__ == "__main__":
    recherche()

