import streamlit as st
from py2neo import Graph
from geopy.geocoders import Nominatim
import folium
from streamlit_folium import folium_static 
import pandas as pd
import matplotlib.pyplot as plt
import dict_correspondance
from  dict_correspondance import *
import seaborn as sns
import os





# Création de Neo4jRepository object
neo4j_uri       = os.environ.get('neo4j_uri')
neo4j_user      = os.environ.get('neo4j_user')
neo4j_password  = os.environ.get('neo4j_password')

try:
    URI = st.secrets['neo4j_uri']
    AUTH = (st.secrets['neo4j_user'], st.secrets['neo4j_password'])
except:
    URI = neo4j_uri
    AUTH = (neo4j_user, neo4j_password)
    

# Connexion à la base de données Neo4j
graph = Graph(URI, auth=AUTH)

st.write("# Bienvenue sue l'application de suivi des accidents de la route en France 👋")
# st.sidebar.success("Navigez pour voir le contenu")

st.markdown('''Nos données proviennent du fichier national des accidents corporels de la circulation administré par \
    l’Observatoire National Interministériel de la Sécurité Routière disponibles sur le site data.gouv.fr . \
        Il s’agit de données ouvertes répertoriant l’intégralité des accidents corporels survenus durant \
            une année précise en France Métropolitaine, dans les DOM et TOM. On y retrouve 4 fichiers différents : 

Informations de localisation de l’accident,  

Informations concernant les caractéristiques de l’accident,  

Informations sur les victimes 

Les véhicules impliqués.  



Compte tenu de certains indicateurs mis à jour à partir de 2019, il est préconisé de ne pas comparer les données à \
    partir de 2019 avec celles des années précédentes. Ceci explique notre horizon temporel (2019-2021).  

Ces jeux de données sont riches et très intéressants car ils brassent depuis plus de 15 ans un nombre important de\
     variables de tous genres. Ils sont mis à jour annuellement et sont d’un intérêt général.  
 
 L'exploitation des données est faite avec Neo4j, un système de gestion de base de données au code source libre basé \
    sur les graphes, développé en Java par la société Neo technology. Le produit existe depuis 2000, la version 1.0 \
        est sortie en février 2010 (source wikipedia)
 ''')


st.write(''' ## Accident ayant impliqué le plus de véhicules et de victimes  ''')

# Convertir l'adresse en coordonnées
# latitude, longitude = geocode_address(address)
# print(latitude, longitude)
# Exécuter la requête Neo4j pour trouver les accidents dans un rayon autour de l'adresse
query = f"""        
MATCH (n)
RETURN n, size([(n)-[r]->() | r]) as degree
ORDER BY degree DESC
LIMIT 1;
"""

results  = graph.run(query).to_data_frame()
df  = pd.DataFrame.from_records(results['n'])



# Afficher les résultats de la requête sous forme de graphe Neo4j
st.subheader("Résultats de la requête")




# Transformer les données : 

df['Date'] = df['An'].astype('str') + '-' + df['Mois'].astype('str') + '-' + df['Jour'].astype('str') + ' ' + df['Heure']
df.insert(0, 'Date', df.pop('Date'), allow_duplicates=False)
df['Date'] = pd.to_datetime(df['Date']) 
df.drop(columns=['An', 'Mois', 'Jour', 'Heure'], inplace=True)       

# for titre in df.columns:
#     try:
#         df[str(titre)] = df[str(titre)].astype('int')
#     except:
#         st.write(titre, 'not converted')
#         continue


dc = dict_correspondance.__dict__ 
# st.write(d)

# Récupération des correspondances
def trouv_corresp(df):
    for titre in df.columns:
        try:
            df[titre] = df[titre].astype('int')
        except:
            continue

    for col in df.columns:
        try:
            ref = dc[col]
            ref = dic_convert(ref)            
            for k,v in ref.items():
                print("cle : ", k,", val : ", v, "col :", col )
                df[col].replace(v, k.replace('_', " "), inplace=True)
        except :
            continue 
    return df
df1 = trouv_corresp(df)

st.write(df1)


# df["Adresse_postale"] = df.Adresse_postale.str.replace("  ", "")





