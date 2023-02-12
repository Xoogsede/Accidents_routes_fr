from Accueil import *
import fonctions as fc

st.write(''' # 6 - Classement des fréquences d'accident par années et mois entre 2019 et 2021 ''')

# st.write(''' ### Voici les 5 départements les plus accidentogènes et, sans surprise, Paris arrive en tête.''')

palette = fc.sns.color_palette('mako_r' , 12)

fig = fc.plt.figure(figsize = (10, 5)) 
ax = fc.sns.barplot(x='Annee',  y='nombre_accident', hue='mois', data=df6, 
                    order=df6.sort_values('Annee', ascending=True).Annee.unique(), palette=palette)
ax.set_xticklabels(ax.get_xticklabels(), rotation = 90)

# for i in ax.containers:
#     ax.bar_label(i,)
st.pyplot(fig)


st.write(''' ## Fréquences d'accident par année et mois entre 2019 et 2021 en fonction du nombre de personnes impliquées et de leur état ''')
for titre in df7.columns:
    if titre not in ['Annee', 'mois', "nombre_accident"]:
        st.write(titre.replace("_", " ").replace("nombre", "Nombre de"))
        fig = fc.plt.figure(figsize = (10, 5)) 
        ax = fc.sns.barplot(x='Annee',  y=titre, hue='mois', 
                            data=df7, order=df7.sort_values('Annee', 
                            ascending=True).Annee.unique(), palette=palette)
        ax.set_xticklabels(ax.get_xticklabels(), rotation = 90)

        st.pyplot(fig)

st.write("Données", df7)