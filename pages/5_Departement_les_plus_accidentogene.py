from Accueil import *
from fonctions import *

st.write(''' # 3 - Département les plus accidentogènes :  ''')
st.write(df5)
# query5 = qr.query_stat(acci_num5)

# implique5 = fc.total_implique(graph, query5[0])

# df51, _ = fc.data_query_transform(graph=graph, query=query5[1], dictionnaire=dc)
# df52, _ = fc.data_query_transform(graph=graph, query=query5[2], dictionnaire=dc)
# df53, _ = fc.data_query_transform(graph=graph, query=query5[3], dictionnaire=dc)

# vhl5 = df53['catv'].value_counts().reset_index()

# grav_par_age = df12
fig = plt.figure(figsize = (10, 5)) 
ax = sns.barplot(x='Departement',  y='nb_victimes', data=df5, order=df5.sort_values('nb_victimes', ascending=False).Departement)
for i in ax.containers:
    ax.bar_label(i,)
# sns.stripplot(x="Departement", y='nb_victimes', data=df5)


st.pyplot(fig)


# st.write('''##### les 5 départements les plus accidentogènes sont''', (j.Departement, j.nb_victimes) for i, j in df5.iterrows())
#df5['Departement'][0], df5['Departement'][1], df5['Departement'][2], df5['Departement'][3] et df5['Departement'][4])

