from Accueil import *


def tb(df_nb):
    
    st.write('''#### Usagers et Véhicules impliqués impliqué dans l'accident''', eval('df' + str(df_nb) + '1'))

    st.write('''#### Usagers impliqués impliqué dans l'accident''', eval('df' + str(df_nb) + '2'))

    st.write('''#### Véhicules impliqués impliqué dans l'accident''', eval('df' + str(df_nb) + '3'))
    return None

st.write(''' ## Accident ayant impliqué le plus de véhicules et de victimes  ''', df1)
st.write(implique1.Nombre[0]," usagers impliqués, majoritairement des  ", implique1)
tb(1)
st.write(''' ## Accident ayant impliqué le plus de victimes  ''', df2)
st.write(implique1.Nombre[0]," usagers impliqués, majoritairement des ")
tb(2)