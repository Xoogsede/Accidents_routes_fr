from Accueil import *

st.write(''' # 2 - Accident ayant impliqué le plus de victimes :  ''')

query2 = qr.query_stat(acci_num2)

implique2 = fc.total_implique(graph, query2[0])

df21, _ = fc.data_query_transform(graph=graph, query=query2[1], dictionnaire=dc)
df22, _ = fc.data_query_transform(graph=graph, query=query2[2], dictionnaire=dc)
df23, _ = fc.data_query_transform(graph=graph, query=query2[3], dictionnaire=dc)

vhl2 = df23['catv'].value_counts().reset_index()


st.write('''##### L'accident ayant impliqué le plus de victimes depuis 2019 s’est produit dans le département ''', df2['Département'][0],''', plus \
précisément sur la''', df2.Adresse_postale[0], df2.Commune[0],''' et a impliqué ''', 
implique2.Nombre[0], implique2.type[0][0].lower()+'s',''' dont ''', vhl2.iloc[0,1], ''' 🚴🏻‍♂️ et ''', implique2.Nombre[1], implique2.type[1][0].lower()," dont ",vhl2.iloc[0,1], " ", str(vhl2.iloc[0,0]).lower()+'s et ', vhl2.iloc[1,1], ' '+ str(vhl2.iloc[1,0]).lower()+'s.','''\
    Cet accident s’est produit le ''', df2.Date[0]," à ", df2.Heure[0],''', hors intersection \
        sous des  ''', str(df2['Conditions_atmosphériques'].name).replace('_', ' ').lower() + ' dites ', str(df2['Conditions_atmosphériques'][0]).lower()+'s','''.''')


fc.stat_loc_data(implique2, df2, df22, df23)
