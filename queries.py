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

# Classement des fréquences d'accident par année et mois entre 2019 et 2022
query8 = f'''
MATCH (n:Accident) 
RETURN n.An as Annee,n.Mois AS mois, COUNT (*) AS nombre_accident 
ORDER BY nombre_accident DESC;'''


# Classement des fréquences d'accident par année et mois entre 2019 et 2022 en fonction du nombre de personnes impliquées et de leur état
query9 = f'''
MATCH (u:Usager)-[r:EST_CONCERNE]->(a:Accident)
RETURN ToInteger(a.An) AS Annee,ToInteger(a.Mois) AS mois, 
    COUNT (distinct(a.Num_Acc)) AS nombre_accident , 
    COUNT (a.Num_Acc)AS nombre_personne_impliqué,
    SUM(CASE WHEN(u.grav="1") THEN 1 ELSE 0 END) AS indimnes,
    SUM(CASE WHEN(u.grav="2") THEN 1 ELSE 0 END) AS décédés,
    SUM(CASE WHEN(u.grav="3") THEN 1 ELSE 0 END) AS hospitalisés,
    SUM(CASE WHEN(u.grav="4") THEN 1 ELSE 0 END) AS légers,
    SUM(CASE WHEN(u.grav=" -1") THEN 1 ELSE 0 END) AS non_renseignés
ORDER BY nombre_accident DESC;
'''


# Profil Conducteur les plus à risque
query10 = f'''
MATCH (u:Usager)-[r:EST_CONCERNE]->(a:Accident) 
WHERE a.An IS NOT NULL // à modifier si 
AND  u.an_nais IS NOT NULL 
AND u.catu = "1" 
    RETURN  CASE WHEN u.sexe="1" THEN"Homme"
        ELSE CASE WHEN u.sexe="2" THEN "Femme" ELSE "Non renseigné" END 
        END AS sexe, 
        (ToInteger(a.An)-Tointeger(u.an_nais)) AS Age,
        COUNT(*) AS nb_accident 
        ORDER BY nb_accident DESC
'''


# lieux des accidents en fonction des catégories de route sur les 5 départements en Hauts-de-France : Aisne (02),Nord (59),Oise (60),Pas-de-Calais (62),Somme (80)
query11 = f'''
WITH ["59", "62", "80", "02", "60"] as dep
MATCH (a:Accident)
WHERE ANY (i IN dep WHERE i = a.`Département`) 
MATCH (a:Accident)-[:EST_LOCALISE]->(l:Lieux)
RETURN CASE l.Categorie 
WHEN "1" THEN "Autoroute" 
      WHEN "2" THEN"Route_nationale" 
         WHEN "3" THEN"Route_Departementale"
             WHEN "4" THEN "Voie_Communales"
                 WHEN  "5" THEN "Hors_reseau_public"
                     WHEN "6" THEN "Parc_de_stationnement_ouvert_a_la_circulation_publique"
                         WHEN "7" THEN "Routes_de_metropole_urbaine" 
                             WHEN "9" THEN "autre__voie__Numero_de_la_route." 
                                 END AS Catégorie_route , count(a.Num_Acc) AS nb_accident
'''