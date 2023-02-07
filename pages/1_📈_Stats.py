from Accueil import *



st.title("Statistique")

total_accident = df1[["Type_de_collision"]].count().tolist()[0]
st.write(''' ## Accident ayant impliqué ''', implique1.Nombre[0], implique1.type[0][0].lower()+'s',''' et ''', implique1.Nombre[1], implique1.type[1][0].lower())

# st.write(df1)
annee_accid = df1['Date'].dt.year[0]
df12['age'] = annee_accid - df12['an_nais']
df12.insert(0, 'age', df12.pop('age'), allow_duplicates=False)

st.subheader("Gravité de l'accident en fonction de l'age")
# grav_par_age = df12
fig = plt.figure(figsize = (10, 5)) 
sns.boxplot(x='age',  y='grav', hue='sexe', data=df12)
sns.stripplot(x="age", y='grav', hue='sexe', data=df12)


st.pyplot(fig)

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
