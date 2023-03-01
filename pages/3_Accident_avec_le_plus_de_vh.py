from Accueil import *
import fonctions as fc

st.write(''' # 3 - Accident ayant impliqué le plus de véhicules :  ''')

query3 = qr.query_stat(acci_num3)

implique3 = fc.total_implique(graph, query3[0])

df31, _ = fc.data_query_transform(graph=graph, query=query3[1], dictionnaire=dc)
df32, _ = fc.data_query_transform(graph=graph, query=query3[2], dictionnaire=dc)
df33, _ = fc.data_query_transform(graph=graph, query=query3[3], dictionnaire=dc)

vhl3 = df33['catv'].value_counts().reset_index()


st.write('''##### L'accident ayant impliqué le plus de véhicules depuis 2019 s’est produit dans le département ''', df3['Département'][0],''', plus \
précisément sur la''', df3.Adresse_postale[0], df3.Commune[0],''' et a impliqué ''', 
implique3.Nombre[0], implique3.type[0][0].lower()+'s',''' dont ''', vhl3.iloc[0,1], ''' 🚴🏻‍♂️ et ''', implique3.Nombre[1], implique3.type[1][0].lower()," dont ",vhl3.iloc[0,1], " ", str(vhl3.iloc[0,0]).lower()+'s et ', vhl3.iloc[1,1], ' '+ str(vhl3.iloc[1,0]).lower()+'s.','''\
    Cet accident s’est produit le ''', df3.Date[0]," à ", df3.Heure[0],''', hors intersection \
        sous des  ''', str(df3['Conditions_atmosphériques'].name).replace('_', ' ').lower() + ' dites ', str(df3['Conditions_atmosphériques'][0]).lower()+'s','''.''')


fc.stat_loc_data(implique3, df3, df32, df33)