from Accueil import *
import fonctions as fc

st.write(''' # 6 - Profil Conducteur les plus à risque ''')



df8.dropna(inplace=True)
df8['Age'] = df8['Age'].astype('int')
grouped = df8.sort_values('Age').groupby(['sexe'])
grouped_cumulative_sum = grouped['nb_accident'].cumsum()
df8['Somme_cumulée'] = grouped_cumulative_sum

st.subheader('Les accidents en fonctions des ages')

palette = fc.sns.color_palette('mako_r' , 12)
fc.sns.set_theme(style="whitegrid")
fig, ax = fc.plt.subplots(1, 1, figsize = (10, 5), dpi=300) 
fc.sns.lineplot(data=df8.sort_values(['Age'], ascending=True), 
                    x='Age', y='nb_accident', hue='sexe', hue_order=df8.sexe.sort_values().unique(), palette="tab10", linewidth = 2.5)
ax.set_xticklabels(ax.get_xticklabels(), rotation = 45)
st.pyplot(fig)
st.markdown('''Les jeunes hommes de 19 à 24 ans sont les plus impliqués dans les accidents.''')

st.markdown('''
''')

# # Calcul de la moyenne d'âge par sexe
mean_age_by_sexe =  fc.pd.DataFrame(df8.groupby('sexe').apply(lambda x: fc.np.average(x['Age'], weights=x['nb_accident']))).rename(columns={0:"moyenne"})

# Calcul de la médiane pondérée par les fréquences par sexe
median_age_by_sexe = fc.pd.DataFrame(df8.groupby('sexe').apply(lambda x: fc.np.median(fc.np.repeat(x['Age'], x['nb_accident'])))).rename(columns={0:"mediane"})

dispertion = fc.pd.DataFrame(df8.groupby('sexe').apply(lambda x: fc.np.repeat(x['Age'], x['nb_accident']))).sort_values(['Age']).reset_index()
# Calcul du premier quartile (Q1)

q1 = dispertion.groupby(['sexe']).apply(lambda x: fc.np.percentile(x['Age'], 25))

# Calcul du troisième quartile (Q3)
q3 = dispertion.groupby(['sexe']).apply(lambda x: fc.np.percentile(x['Age'], 75))

# Calcul de l'IQR
iqr = q3 - q1

st.subheader('Dispersion des accidents par age')
fig, ax = fc.plt.subplots(1, 1, figsize = (10, 5), dpi=300) 
fc.sns.boxplot(data=dispertion, 
                    x='Age', y='sexe', hue_order=df8.sexe.sort_values().unique())
ax.set_xticklabels(ax.get_xticklabels(), rotation = 45)

ax.legend()
ax.set_xlabel('Age')
ax.set_ylabel('Sexe')
st.pyplot(fig)

st.markdown('''##### 
50 pourcent des accidents concerna la tranche d'age 26 - 51 pour les hommes et 26 - 53.
Cela signifie que 25 \% des accidents concernes les jeunes de moins de 26''')

mean = df8.groupby(['sexe'])['Somme_cumulée'].mean()
median = df8.groupby(['sexe'])['Somme_cumulée'].median()
# st.write(mean, median)

# Calculer la somme cumulative, la moyenne et la médiane pour chaque groupe

grouped_mean = grouped['nb_accident'].mean()
grouped_median = grouped['nb_accident'].median()

# Ajouter les statistiques à la figure
color_means = fc.sns.color_palette("deep", 3)
color_medians = fc.sns.color_palette("bright", 3)
label_offset = 50000
position_label_moyenne = [150000, 100000, 50000,]
position_label_mediane = [170000, 80000, 65000]

st.markdown('''
''')
st.subheader('Fréquences cumulées des accidents par sexe')
st.markdown('''##### 
L'age moyen et l'age médian sont assez proches pour les hommes comme pour les femmes impliqués dans les accidents.''')
fig, ax = fc.plt.subplots()
fc.sns.lineplot(data=df8, x='Age', y="Somme_cumulée", hue="sexe")
for i, sexe in enumerate(df8.sexe.unique()):
    mean_age = mean_age_by_sexe.loc[sexe][0]
    fc.plt.axvline(x=mean_age, color=color_means[i % len(color_means)])
    fc.plt.annotate(f"{sexe} : moyenne d\'age {mean_age:.2f}", xy=(mean_age, position_label_moyenne[i]), 
    xytext=(mean_age + 6, position_label_moyenne[i]), ha='left', va='center', 
    color=color_means[i % len(color_means)], fontsize=14, arrowprops=dict(facecolor=color_means[i % len(color_means)], shrink=0.05))
    
    age_median = median_age_by_sexe.loc[sexe][0]
    fc.plt.axvline(x=age_median,color=color_medians[i % len(color_medians)] )
    fc.plt.annotate(f"{sexe} : age médian {age_median:.2f}", xy=(age_median, position_label_mediane[i]), 
    xytext=(age_median + 6, position_label_mediane[i]), ha='left', va='center', 
    color=color_medians[i % len(color_medians)], fontsize=14, arrowprops=dict(facecolor=color_medians[i % len(color_medians)], shrink=0.05))
ax.legend()
ax.set_xlabel('Age')
ax.set_ylabel('Nombre d\'accident')

st.pyplot(fig)
