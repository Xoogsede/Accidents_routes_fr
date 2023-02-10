import streamlit as st
from py2neo import Graph
from geopy.geocoders import Nominatim
import folium
from streamlit_folium import folium_static 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import dict_correspondance as dc
# from  dict_correspondance import *
import time
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

# time.sleep(15)
# from fonctions import fc.data_query_transform as fc.data_query_transform, total_implique as tot
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
# st.sidebar.success("Navigez pour voir le contenu")

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

 ''')

st.write('''   ''')

st.write(''' ''')


st.write(''' ### 1 - Accident ayant impliqué le plus de véhicules et de victimes :  ''')


df1, acci_num1 = fc.data_query_transform(graph=graph, query=qr.query, dictionnaire=dc)


st.session_state['df1'] = df1


# df["Adresse_postale"] = df.Adresse_postale.str.replace("  ", "")



query1 = qr.query_stat(acci_num1)

implique1 = fc.total_implique(graph, query1[0])

df11, _ = fc.data_query_transform(graph=graph, query=query1[1], dictionnaire=dc)
df12, _ = fc.data_query_transform(graph=graph, query=query1[2], dictionnaire=dc)
df13, _ = fc.data_query_transform(graph=graph, query=query1[3], dictionnaire=dc)

vhl2 = df13['catv'].value_counts().reset_index()


st.write('''##### Cet accident s’est produit dans le département ''', df1['Département'][0],''', plus \
précisément sur la''', df1.Adresse_postale[0], df1.Commune[0],''' et a impliqué ''', 
implique1.Nombre[0], implique1.type[0][0].lower()+'s',''' dont ''', vhl2.iloc[0,1], ''' 🚴🏻‍♂️ et ''', implique1.Nombre[1], implique1.type[1][0].lower()," dont ",vhl2.iloc[0,1], " ", str(vhl2.iloc[0,0]).lower()+'s et ', vhl2.iloc[1,1], ' '+ str(vhl2.iloc[1,0]).lower()+'s.','''\
    Cet accident s’est produit le ''', df1.Date[0]," à ", df1.Heure[0],''', hors intersection \
        sous des ''', str(df1['Conditions_atmosphériques'].name).replace('_', ' ').lower() + ' dites ', str(df1['Conditions_atmosphériques'][0]).lower(),'''.  

En lien, l’article faisant référence à ce sinistre. 

https://www.le-pays.fr/saint-just-saint-rambert-42170/faits-divers/une-quinzaine-de-cyclistes-heurtes-par-une-voiture-entre-saint-cyprien-et-saint-just-saint-rambert_13928751/

  ''')



df2, acci_num2 = fc.data_query_transform(graph=graph, query=qr.query5, dictionnaire=dc)

query2 = qr.query_stat(acci_num2)

implique2 = fc.total_implique(graph, query2[0])

df21, _ = fc.data_query_transform(graph=graph, query=query2[1], dictionnaire=dc)
df22, _ = fc.data_query_transform(graph=graph, query=query2[2], dictionnaire=dc)
df23, _ = fc.data_query_transform(graph=graph, query=query2[3], dictionnaire=dc)

vhl2 = df23['catv'].value_counts().reset_index()

st.write(''' ### 2 - Accident ayant impliqué le plus de victimes :  ''')

st.write('''##### Cet accident s’est produit dans le département ''', df2['Département'][0],''', plus \
précisément sur la''', df2.Adresse_postale[0], df2.Commune[0],''' et a impliqué ''', 
implique2.Nombre[0], implique2.type[0][0].lower()+'s',''' dont ''', vhl2.iloc[0,1], ''' 🚴🏻‍♂️ et ''', implique2.Nombre[1], implique2.type[1][0].lower()," dont ",vhl2.iloc[0,1], " ", str(vhl2.iloc[0,0]).lower()+'s et ', vhl2.iloc[1,1], ' '+ str(vhl2.iloc[1,0]).lower()+'s.','''\
    Cet accident s’est produit le ''', df2.Date[0]," à ", df2.Heure[0],''', hors intersection \
        sous des  ''', str(df2['Conditions_atmosphériques'].name).replace('_', ' ').lower() + ' dites ', str(df2['Conditions_atmosphériques'][0]).lower()+'s','''.''')

