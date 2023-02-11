from Accueil import *

st.write(''' # 1 - Accident ayant impliqué le plus de véhicules et de victimes depuis 2019 🚶🏽💥🚗 :  ''')

query1 = qr.query_stat(acci_num1)

implique1 = fc.total_implique(graph, query1[0])

df11, _ = fc.data_query_transform(graph=graph, query=query1[1], dictionnaire=dc)
df12, _ = fc.data_query_transform(graph=graph, query=query1[2], dictionnaire=dc)
df13, _ = fc.data_query_transform(graph=graph, query=query1[3], dictionnaire=dc)

vhl1 = df13['catv'].value_counts().reset_index()


st.write('''#####  L'accident ayant impliqué le plus de véhicules et de victimes depuis 2019 s’est produit dans le département ''', df1['Département'][0],''', plus \
précisément sur la''', df1.Adresse_postale[0], df1.Commune[0],''' et a impliqué ''', 
implique1.Nombre[0], implique1.type[0][0].lower()+'s',''' dont ''', vhl1.iloc[0,1], ''' 🚴🏻‍♂️ et ''', implique1.Nombre[1], implique1.type[1][0].lower()," dont ",vhl1.iloc[0,1], " ", str(vhl1.iloc[0,0]).lower()+'s et ', vhl1.iloc[1,1], ' '+ str(vhl1.iloc[1,0]).lower()+'s.','''\
    Cet accident s’est produit le ''', df1.Date[0]," à ", df1.Heure[0],''', hors intersection \
        sous des ''', str(df1['Conditions_atmosphériques'].name).replace('_', ' ').lower() + ' dites ', str(df1['Conditions_atmosphériques'][0]).lower(),'''.  

En lien, l’article faisant référence à ce sinistre. 

https://www.le-pays.fr/saint-just-saint-rambert-42170/faits-divers/une-quinzaine-de-cyclistes-heurtes-par-une-voiture-entre-saint-cyprien-et-saint-just-saint-rambert_13928751/

  ''')


fc.stat_loc_data(implique1, df1, df12, df13)


# st.subheader("Typologie d'accident")  
# fig = plt.figure(figsize = (10, 5))           

# ax = sns.countplot(x = 'Type_de_collision', hue='sexe', data = df1)
# ax.set_xticklabels(ax.get_xticklabels(), rotation = 90)
# ax.set_title("Catégorie d'accident")
# ax.set_xlabel("Type d'accident")
# ax.set_ylabel("Nombre d'accident")

# st.pyplot(fig)



# # Conditions atmosphérique
# st.subheader("Conditions météo lors des accidents")
# fig = plt.figure(figsize = (10, 5))                     

# ax = sns.countplot(x = 'Conditions_atmosphériques', hue='sexe', data = df1)
# ax.set_xticklabels(ax.get_xticklabels(), rotation = 90)
# ax.set_title("Conditions atmosphériques")
# ax.set_xlabel("Conditions météo")
# ax.set_ylabel("Nombre d'accident")
# st.pyplot(fig)

# st.subheader("Catégories des véhicules")
# fig = plt.figure(figsize = (10, 5))                     

# ax = sns.countplot(x = 'catv', hue='sexe', data = df1)
# ax.set_xticklabels(ax.get_xticklabels(), rotation = 90)
# ax.set_title("Catégories des véhicules impliqués")
# ax.set_xlabel("Conditions météo")
# ax.set_ylabel("Nombre d'accident")
# st.pyplot(fig)
