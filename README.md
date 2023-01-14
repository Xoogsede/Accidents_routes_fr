# Accidents_routes_fr
Projet porte sur les accidents de la route en France.
C'est une application web qui utilise Streamlit et Py2neo pour créer une interface utilisateur pour rechercher des accidents de la route en utilisant une base de données Neo4j.  
Les utilisateurs peuvent saisir une adresse postale et un rayon de recherche, l'application utilise l'API de géolocalisation Nominatim pour convertir l'adresse en coordonnées latitude / longitude. 
Ensuite, il exécute une requête Neo4j pour trouver les accidents dans un rayon autour de l'adresse, affiche les résultats de la requête sous forme de tableau et utilise la bibliothèque Folium pour afficher les résultats sur une carte. 
Il utilise également les librairies pandas, matplotlib, seaborn, json et dict_correspondance pour une analyse des données.  
Les utilisateurs peuvent filtrer les résultats en utilisant des dates de début et de fin. 
Les résultats sont affichés sur une carte pour une visualisation plus facile.  
Ce projet est open-source et disponible sur GitHub pour toute personne qui souhaite contribuer ou utiliser le code pour ses propres projets. 
Il est recommandé d'avoir une connaissance de base en Python, Neo4j, Streamlit et Py2neo pour utiliser et comprendre le code.
