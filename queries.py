query = f"""        
MATCH (n)
RETURN n, size([(n)-[r]->() | r]) as degree
ORDER BY degree DESC
LIMIT 1;
"""
# from Accueil import acci_num1

def query_stat(accident_number):

    q1 = f'''
    MATCH (a:Accident{{Num_Acc: {accident_number} }})-[r]-(x) 
    WHERE type(r) <> "EST_LOCALISE"
    RETURN   labels(x) as type, count(*) as Nombre
    ORDER BY Nombre DESC
    '''

    q2 = f'''
    MATCH (a:Accident{{Num_Acc: {accident_number} }})-[r]-(x) 
    WHERE type(r) <> "EST_LOCALISE"
    RETURN   x
    '''

    q3 = f'''
    MATCH (a:Accident{{Num_Acc: {accident_number} }})-[r]-(x) 
    WHERE type(r) <> "EST_LOCALISE" and type(r) <> "IMPLIQUE"
    RETURN   x
    '''

    q4 = f'''
    MATCH (a:Accident{{Num_Acc: {accident_number} }})-[r]-(x) 
    WHERE type(r) <> "EST_LOCALISE" and type(r) <> "EST_CONCERNE"
    RETURN   x, labels(x)
    '''
    return (q1, q2, q3, q4)


query5 = f'''
MATCH (u:Usager)-[r]->(a:Accident)
WITH a, count(r) as degree
RETURN a, degree
ORDER BY degree DESC
LIMIT 1;'''


# Accident ayant impliqué le plus de véhicules
query6 = f'''
MATCH (a:Accident)-[r]->(v:Vehicules)
WITH a, count(r) as degree
RETURN a, degree
ORDER BY degree DESC
LIMIT 1;'''

# Les 5 départements les plus accidentogène
query7 = f'''
MATCH (a:Accident) RETURN a.`Département` as Departement, count(*) as nb_victimes ORDER BY nb_victimes DESC LIMIT 5
'''