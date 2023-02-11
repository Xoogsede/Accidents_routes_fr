from Accueil import *
from fonctions import *

st.write(''' # 6 - Classement des fréquences d'accident par années et mois entre 2019 et 2021 ''', df6)

# st.write(''' ### Voici les 5 départements les plus accidentogènes et, sans surprise, Paris arrive en tête.''')

fig = plt.figure(figsize = (10, 5)) 
ax = sns.barplot(x='Annee',  y='nombre_accident', hue='mois', data=df6, order=df6.sort_values('Annee', ascending=False).Annee.unique())
ax.set_xticklabels(ax.get_xticklabels(), rotation = 90)

# for i in ax.containers:
#     ax.bar_label(i,)
st.pyplot(fig)


st.write(''' # 6 - Classement des fréquences d'accident par année et mois entre 2019 et 2021 en fonction du nombre de personnes impliquées et de leur état ''', df7)

fig = plt.figure(figsize = (10, 5)) 
ax = sns.barplot(x='Annee',  y='nombre_accident', hue='mois', data=df7, order=df7.sort_values('Annee', ascending=False).Annee.unique())
ax.set_xticklabels(ax.get_xticklabels(), rotation = 90)

# for i in ax.containers:
#     ax.bar_label(i,)
st.pyplot(fig)



# st.write(''' ### Comme on peut le voir sur le visuel, les autres départements sont loin derrière Paris. Contrairement à ce qu'on pourrait s'attendre, le Rhône (69) avec la grande ville de Lyon n'est qu'en 5e position.''')
