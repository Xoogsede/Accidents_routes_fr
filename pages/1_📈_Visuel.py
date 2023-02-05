from app import *



st.title("Statistique")

total_accident = df[["Type_de_collision"]].count().tolist()[0]
st.write(''' ## Total accidents : ''',total_accident)


st.subheader("Typologie d'accident")  
fig = plt.figure(figsize = (10, 5))           

ax = sns.countplot(x = 'Type_de_collision', hue='sexe', data = df)
ax.set_xticklabels(ax.get_xticklabels(), rotation = 90)
ax.set_title("Catégorie d'accident")
ax.set_xlabel("Type d'accident")
ax.set_ylabel("Nombre d'accident")

st.pyplot(fig)



# Conditions atmosphérique
st.subheader("Conditions météo lors des accidents")
fig = plt.figure(figsize = (10, 5))                     

ax = sns.countplot(x = 'Conditions_atmosphériques', hue='sexe', data = df)
ax.set_xticklabels(ax.get_xticklabels(), rotation = 90)
ax.set_title("Conditions atmosphériques")
ax.set_xlabel("Conditions météo")
ax.set_ylabel("Nombre d'accident")
st.pyplot(fig)

st.subheader("Catégories des véhicules")
fig = plt.figure(figsize = (10, 5))                     

ax = sns.countplot(x = 'catv', hue='sexe', data = df)
ax.set_xticklabels(ax.get_xticklabels(), rotation = 90)
ax.set_title("Catégories des véhicules impliqués")
ax.set_xlabel("Conditions météo")
ax.set_ylabel("Nombre d'accident")
st.pyplot(fig)
