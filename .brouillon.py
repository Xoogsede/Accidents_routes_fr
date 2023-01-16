import streamlit as st
from py2neo import Graph, Node, Relationship
import folium
from geopy.geocoders import Nominatim


            # df = pd.DataFrame(results[:][:][0][0])
            # df = df.T.reset_index(drop=True)
            # for j in results[1:]:
            #     n=len(df)
            #     df1 = pd.DataFrame(j)
            #     df1 = df1.T.reset_index(drop=True)
            #     df.loc[n]= df1.iloc[0,:]
            
            # df = pd.DataFrame.from_records(results["a"]).merge(pd.DataFrame.from_records(results["u"]).merge(pd.DataFrame.from_records(results["v"]), how='inner', on='Num_Acc'), how='inner', on='Num_Acc')
            
            # df['An'] = df.An.astype('int')
            # df['Mois'] = df.Mois.astype('int')
            # df['Jour'] = df.Jour.astype('int')
            # df['Heure'] = pd.to_datetime(df['Heure'], format='%H:%M', errors='ignore').dt.time
            print(df.An.dtype,df.Mois.dtype, df.Jour.dtype, df.Heure.dtype, "a garder")
            # df['Date'] = pd.to_datetime(df[['An', 'Mois', 'Jour']])
            # year=df.An, month=df.Mois, day = df.Jour, time = df.Heure


graph = Graph(
    host="bolt://localhost:7687",
    user="neo4j",
    password="word"
)
st.set_page_config(page_title="Accidents", page_icon=":tada", layout="wide")

with st.container():
    st.subheader("Bonjour et bienvenue !")
    st.title("Lieux des accidents de la route en France")
    st.write("Vous trouverez ici tous les accidents de la route en France depuis 2019")
    st.write("Si vous souhaitez savoir s'il y a beacoup d'accident autour d'une adresse, vous êtes au bon endroit !")
    st.sidebar
    address = st.text_input("Adresse postale")
    distance = st.number_input("Distance (km)", min_value=0, max_value=100, step=0.1)
    if st.button("Rechercher"):
    # Utilisez Py2neo pour exécuter la requête Cypher
        query = f"MATCH (a:Accident) WHERE distance(point({address}), point({a.Latitude}, {a.Longitude})) < {distance}*1000 RETURN a"
        result = run_query(query)
        st.write("Résultats de la recherche :", result)
    
    
def get_accidents(address, distance):
    query = f"""
    MATCH (a:Accident)
    WHERE a.Adresse_postale = '{address}'
    RETURN a.Num_Acc as Num_Acc, a.Latitude as Latitude, a.Longitude as Longitude, point({longitude: a.Latitude, latitude: a.Longitude}).distance(point({longitude: 20.9310800000, latitude: 55.5372190000})) as distance
    ORDER BY distance
    LIMIT {distance}
    """
    return graph.run(query).data()

def geocode_address(address):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(address)
    return location.latitude, location.longitude

# Create a function to execute Cypher query
def run_query(query):
    return graph.run(query).data()
    


f"""
        MATCH (a:Accident)
        WHERE point({{latitude: {latitude}, longitude: {longitude}}}).distance(point({{latitude: a.Latitude, longitude: a.Longitude}})) < {radius}
        RETURN a
        """
        