import streamlit as st
# import dict_correspondance as dc
# import Accueil as ac
import pandas as pd
import locale

# Définir la langue en français
locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')



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
        df['Date'] = df['An'].astype('str') + '-' + df['Mois'].astype('str') + '-' + df['Jour'].astype('str') + ' ' + df['Heure']
        df.insert(0, 'Date', df.pop('Date'), allow_duplicates=False)
        
        df.drop(columns=['An', 'Mois', 'Jour', 'Heure'], inplace=True)       


        df = trouv_corresp(df)
        df['Date'] = pd.to_datetime(df['Date'])
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
        df['Date'] = pd.to_datetime(df['Date'])
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

