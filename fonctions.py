import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static 
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from babel.dates import format_date

# funcion qui permet de s'assurer que les clés des dictionnaire sont bien les integer
# utilisé dans le tableau 
def dic_convert(dictionnaire):
	new_dict = {}
	for k, v in dictionnaire.items():					
		if (len(str(k)) < len(str(v))):
			new_dict[v]=k			
		else:
			new_dict = dictionnaire
	
	return new_dict



# Récupération des correspondances


def trouv_corresp(df, dictionnaire, dc_list):
    '''
    Converti les codes en claire dans un tableau
    Elle prend en entré un dataframe et le dictionnaire des correspondances '''
    
    for titre in df.columns:
        if titre != "Date":
            try:
                df[titre] = df[titre].astype('int64')
            except:
                continue

    for col in df.columns:
        try:
            if col in dictionnaire.Vehicules.keys():
                ref = dic_convert(dictionnaire.Vehicules[col]) 
            elif col in dictionnaire.Usagers.keys():
                 ref = dic_convert(dictionnaire.Usagers[col])
            else:
                ref = dc_list[col]
                ref = dic_convert(ref)       
            for k,v in ref.items():
                df[col].replace(v, k.replace('_', " "), inplace=True)
        except :
            continue 
    return df


# from Accueil import graph
def data(graph, query):
    results_query  = graph.run(query).to_data_frame()
    
    df  = pd.DataFrame.from_records(results_query.iloc[:,0])
    # Transformation de la date 
    try:
        df['DateTime'] = df['An'].astype('str') + '-' + df['Mois'].astype('str') + '-' + df['Jour'].astype('str') + ' ' + df['Heure']
        df.insert(0, 'DateTime', df.pop('DateTime'), allow_duplicates=False)
        
        df.drop(columns=['An', 'Mois', 'Jour'], inplace=True)       


        df = trouv_corresp(df)
        df['DateTime'] = pd.to_datetime(df['DateTime'])
        df['Date'] = df['DateTime'].apply(lambda x: format_date(x, format='full', locale='fr_FR'))
        df.fillna(-1, inplace=True)
        acci_num = df.Num_Acc[0]
    except:
        df.fillna(-1, inplace=True)
        try: 
            acci_num = df.Num_Acc[0]
        except: 
            acci_num = None
    return (df, acci_num)


def data_query_transform(graph, query, dictionnaire):
    dc_list = dictionnaire.__dict__
    df, acci_num = data(graph, query)
    df = trouv_corresp(df, dictionnaire, dc_list)
    try:
        df['DateTime'] = pd.to_datetime(df['DateTime'])
        df['Date'] = df['DateTime'].apply(lambda x: format_date(x, format='full', locale='fr_FR'))
    except:
        pass
    return (df, acci_num)


def total_implique(graph, query):
    
    df=graph.run(query).to_data_frame()
    implique = pd.DataFrame.from_records(df)

    return implique


def _max_width_(prcnt_width:int = 75):
    max_width_str = f"max-width: {prcnt_width}%;"
    st.markdown(f""" 
                <style> 
                .reportview-container .main .block-container{{{max_width_str}}}
                </style>    
                """, 
                unsafe_allow_html=True,
    )


def tb(df1, df2):
    st.write('''#### Usagers impliqués impliqué dans l'accident''', df1)

    st.write('''#### Véhicules impliqués impliqué dans l'accident''', df2)
    return None


def stat_loc_data(implique1, df1, df12, df13):
        
    st.write('''   ''')

    st.write(''' ''')


    st.title("📈 Statistique 📊")

    total_accident = df1[["Type_de_collision"]].count().tolist()[0]
    st.write(''' ## Accident ayant impliqué ''', implique1.Nombre[0], implique1.type[0][0].lower()+'s',''' et ''', implique1.Nombre[1], implique1.type[1][0].lower())

    # st.write(df1)
    annee_accid = df1['DateTime'].dt.year[0]
    df12['age'] = annee_accid - df12['an_nais']
    df12.insert(0, 'age', df12.pop('age'), allow_duplicates=False)

    st.subheader("Gravité de l'accident en fonction de l'age")
    # grav_par_age = df12
    fig = plt.figure(figsize = (10, 5)) 
    sns.boxplot(x='age',  y='grav', hue='sexe', data=df12)
    sns.stripplot(x="age", y='grav', hue='sexe', data=df12)


    st.pyplot(fig)


    st.write('''   ''')

    st.write('''   ''')

    # Afficher les résultats sur une carte
    st.title("🌍 Localisation géographique 🌍")        
    # Création de la carte
    map = folium.Map(location=[df1['Latitude'], df1['Longitude']], zoom_start=13)
    folium.Marker([df1['Latitude'], df1['Longitude']], popup=df1.Adresse_postale, tooltip="<strong>"f'{df1.Adresse_postale}'"</strong>", 
                icon=folium.Icon(color='red')).add_to(map)
    # Ajouter les marqueurs pour les accidents
    # for _ , accident in acc[['Latitude', 'Longitude']].iterrows():
    #     folium.Marker([accident['Latitude'], accident['Longitude']]).add_to(map)

    map.save("static/carte.html")

    folium_static(map, width=_max_width_(80), height=800)          


    st.write('''   ''')

    st.write('''   ''')

    st.write(''' # Données de l'accident ''', df1)
    st.write(implique1.Nombre[0]," usagers impliqués, majoritairement des  ", implique1)
    
    tb(df12, df13)

    return None
    


