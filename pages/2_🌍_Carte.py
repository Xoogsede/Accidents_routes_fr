from Accueil import *
from fonctions import _max_width_





# Afficher les résultats sur une carte
st.title("Localisation géographique")        
# Création de la carte
map = folium.Map(location=[df1['Latitude'], df1['Longitude']], zoom_start=13)
folium.Marker([df1['Latitude'], df1['Longitude']], popup=df1.Adresse_postale, tooltip="<strong>"f'{df1.Adresse_postale}'"</strong>", 
            icon=folium.Icon(color='red')).add_to(map)
# Ajouter les marqueurs pour les accidents
# for _ , accident in acc[['Latitude', 'Longitude']].iterrows():
#     folium.Marker([accident['Latitude'], accident['Longitude']]).add_to(map)

map.save("static/carte.html")

folium_static(map, width=_max_width_(80), height=800)            

