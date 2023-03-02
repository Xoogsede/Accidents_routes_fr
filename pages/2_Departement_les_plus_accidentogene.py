from Accueil import *
import fonctions as fc

st.write(''' # 5 - Département les plus accidentogènes :  ''')

st.write(''' ### Voici les 5 départements les plus accidentogènes et, sans surprise, Paris arrive en tête.''')

fig = fc.plt.figure(figsize = (10, 5)) 
ax = fc.sns.barplot(x='Departement',  y='nb_victimes', data=df5, order=df5.sort_values('nb_victimes', ascending=False).Departement)
for i in ax.containers:
    ax.bar_label(i,)
st.pyplot(fig)

st.write(''' ### Comme on peut le voir sur le visuel, les autres départements sont loin derrière Paris. Contrairement à ce qu'on pourrait s'attendre, le Rhône (69) avec la grande ville de Lyon n'est qu'en 5e position.''')
