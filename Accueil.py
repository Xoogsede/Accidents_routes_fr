import streamlit as st
from py2neo import Graph
from geopy.geocoders import Nominatim
import dict_correspondance as dc
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

import  fonctions as fc

st.set_page_config(
    page_title="Accitrack", 
    page_icon="🚨", 
    layout = "wide" 
)

if "df1" not in st.session_state:
    st.session_state["df1"]=""

import queries as qr 


st.write("# Bienvenue dans l'application de suivi des 🚘💥🚗 de la route en France 👋🏾")


st.markdown(''' ###### Les données proviennent du fichier national des acci_num1s corporels de la circulation administré par \
    l’Observatoire National Interministériel de la Sécurité Routière disponibles sur le site www.data.gouv.fr . \
        Il s’agit de données ouvertes répertoriant l’intégralité des acci_num1s corporels survenus durant \
            une année précise en France Métropolitaine, dans les DOM et TOM. On y retrouve 4 fichiers différents : \

##### Informations de localisation de l’accident,  

##### Informations concernant les caractéristiques de l’accident,  

##### Informations sur les victimes 

##### Les véhicules impliqués.  



##### Compte tenu de certains indicateurs mis à jour à partir de 2019, il est préconisé de ne pas comparer les données à \
    partir de 2019 avec celles des années précédentes. Ceci explique notre horizon temporel (2019-2021).  

##### Ces jeux de données sont riches et très intéressants car ils brassent depuis plus de 15 ans un nombre important de\
     variables de tous genres. Ils sont mis à jour annuellement et sont d’un intérêt général.  
 
##### L'exploitation des données est faite avec Neo4j, un système de gestion de base de données au code source libre basé \
    sur les graphes, développé en Java par la société Neo technology. Le produit existe depuis 2000, la version 1.0 \
        est sortie en février 2010 (source wikipedia)

https://amzn.to/3siQDCu

 ''')

st.write('''   ''')

st.write('''   ''')

df1, acci_num1 = fc.data_query_transform(graph=graph, query=qr.query, dictionnaire=dc)

st.session_state['df1'] = df1

df2, acci_num2 = fc.data_query_transform(graph=graph, query=qr.query5, dictionnaire=dc)

df3, acci_num3 = fc.data_query_transform(graph=graph, query=qr.query6, dictionnaire=dc)

df5 = graph.run(qr.query7).to_data_frame()

df6 = graph.run(qr.query8).to_data_frame()

df7 = graph.run(qr.query9).to_data_frame()

df8 = graph.run(qr.query10).to_data_frame()

df9 = graph.run(qr.query11).to_data_frame()

