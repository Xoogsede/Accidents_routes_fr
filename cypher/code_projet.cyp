//Les paramettre à modifier dans le fichier config:

//server.memory.heap.max_size=4096m
//dbms.memory.transaction.total.max=104857600000m
//db.memory.transaction.max=160000000m

// Chargement des données depuis un fichier CSV "caracteristiques.csv"
LOAD CSV WITH HEADERS FROM 'https://github.com/Xoogsede/Accidents_routes_fr/tree/main/data/caracteristiques.csv' AS line FIELDTERMINATOR ";"
WITH line WHERE line.Num_Acc IS NOT NULL // filtrer les lignes qui ont une valeur non nulle pour la propriété Num_Acc
CREATE (a:Accident { 
    Num_Acc : line.Num_Acc,
    Jour : line.jour,
    Mois : line.mois,
    An : line.an,
    Heure : line.hrmn,
    Lumière : line.lum,
    Département : CASE WHEN line.dep='2A' or line.dep='2B' THEN '20'   
                      ELSE CASE WHEN SIZE(line.dep)=1 THEN ("0"+line.dep) 
                                else line.dep END
                  END,
    Commune : line.com,
    Localisation : line.agg,
    Intersection : line.int,
    Conditions_atmosphériques : line.atm,
    Type_de_collision : line.col,
    Adresse_postale : line.adr,
    Latitude : line.lat,
    Longitude : line.long
 })
 RETURN count(*) ;// retourne le nombre de nœuds créés

//Conversion de la latitude et de la longitude en réel (au chargement c'est en chaine de caractère)
MATCH (a:Accident)
SET a.Latitude = toFloat(a.Latitude), a.Longitude = toFloat(a.Longitude);


// créer une contrainte qui garantit que la propriété Num_Acc est unique pour les nœuds de type Accident
CREATE CONSTRAINT FOR (a:Accident) REQUIRE a.Num_Acc IS UNIQUE; 


// création d'index sur les propriété Latitude et Longitude pour améliorer les performances de certaines requêtes.
CREATE INDEX FOR (a:Accident) ON (a.Latitude);
CREATE INDEX FOR (a:Accident) ON (a.Longitude);


// Chargement des données depuis un fichier CSV "lieux.csv"
LOAD CSV WITH HEADERS FROM "https://github.com/Xoogsede/Accidents_routes_fr/tree/main/data/lieux.csv" AS row FIELDTERMINATOR ";"
WITH row WHERE row.Num_Acc IS NOT NULL // filtrer les lignes qui ont une valeur non nulle pour la propriété Num_Acc
CREATE (li:Lieux {
Num_Acc: row.Num_Acc,
Categorie: row.catr,
voie: row.voie,
v1: row.v1,
v2: row.v2,
circ: row.circ,
nbv: row.nbv,
vosp: row.vosp,
prof: row.prof,
pr: row.pr,
pr1: row.pr1,
plan: row.plan,
lartpc: row.lartpc,
larrout: row.larrout,
surf: row.surf,
infra: row.infra,
situ: row.situ,
vma: row.vma
})
RETURN count(*) ; // retourne le nombre de nœuds créés

//Conversion de la latitude et de la longitude en réel (au chargement c'est en chaine de caractère)
MATCH (li:Lieux)
SET li.lartpc = toFloat(li.lartpc), li.larrout = toFloat(li.larrout), li.pr1 = toFloat(li.pr1);

// créer une contrainte qui garantit que la propriété Num_Acc est unique pour les nœuds de type Lieux
CREATE CONSTRAINT FOR (li:Lieux) REQUIRE li.Num_Acc IS UNIQUE; 


// Chargement des données depuis un fichier CSV "usagers.csv"
LOAD CSV WITH HEADERS FROM "https://github.com/Xoogsede/Accidents_routes_fr/tree/main/data/usagers.csv" AS row FIELDTERMINATOR ";"
WITH row WHERE row.Num_Acc IS NOT NULL // filtrer les lignes qui ont une valeur non nulle pour la propriété Num_Acc
CREATE (u:Usager {
Num_Acc: row.Num_Acc,
id_vehicule: row.id_vehicule,
num_veh: row.num_veh,
place: row.place,
catu: row.catu,
grav: row.grav,
sexe: row.sexe,
an_nais: row.an_nais,
trajet: row.trajet,
secu1: row.secu1,
secu2: row.secu2,
secu3: row.secu3,
locp: row.locp,
actp: row.actp,
etatp: row.etatp
})
RETURN count(*); // retourne le nombre de nœuds créés


// créer une contrainte qui garantit que la propriété id est unique pour les nœuds de type Usager
CREATE CONSTRAINT FOR (u:Usager) REQUIRE u.id IS UNIQUE; 

// Chargement des données depuis un fichier CSV "vehicules.csv"
LOAD CSV WITH HEADERS FROM "https://github.com/Xoogsede/Accidents_routes_fr/tree/main/data/vehicules.csv" AS row FIELDTERMINATOR ";"
WITH row WHERE row.Num_Acc IS NOT NULL // filtrer les lignes qui ont une valeur non nulle pour la propriété Num_Acc
CREATE (v:Vehicules {
Num_Acc: row.Num_Acc, 
id_vehicule: row.id_vehicule, 
num_veh: row.num_veh, 
senc: row.senc, 
catv: row.catv, 
obs: row.obs, 
obsm: row.obsm, 
choc: row.choc, 
manv: row.manv, 
motor: row.motor, 
occutc: row.occutc
})
RETURN count(*) ;// retourne le nombre de nœuds créés

MATCH (v:Vehicules)
SET v.occutc = toFloat(v.occutc);

// créer une contrainte qui garantit que la propriété id_vehicule est unique pour les nœuds de type Vehicules
CREATE CONSTRAINT FOR (v:Vehicules) REQUIRE v.id_vehicule IS UNIQUE;


// Création de relations entre les nœuds de type "Usager" et "Vehicules" en utilisant la propriété commune "Num_Acc"
MATCH (u:Usager), (v:Vehicules)
WHERE u.Num_Acc = v.Num_Acc
  MERGE (u)-[:EST_PRESENT]->(v);


// Création de relations entre les nœuds de type "Usager" et "Accident" en utilisant la propriété commune "Num_Acc"
MATCH (u:Usager), (a:Accident)
WHERE u.Num_Acc = a.Num_Acc
  MERGE (u)-[:EST_CONCERNE]->(a);



// Création de relations entre les nœuds de type "Accident" et "Vehicules" en utilisant la propriété commune "Num_Acc"
MATCH (a:Accident), (v:Vehicules)
WHERE a.Num_Acc = v.Num_Acc
  MERGE (a)-[:IMPLIQUE]->(v);


// Création de relations entre les nœuds de type "Accident" et "Lieux" en utilisant la propriété commune "Num_Acc"
MATCH (a:Accident), (l:Lieux)
WHERE a.Num_Acc = l.Num_Acc
  MERGE (a)-[:EST_LOCALISE]->(l);


// Recherche des relations multiples 
MATCH (a)-[r]->(b) WITH a, b, COUNT(r) AS c WHERE c>1 RETURN a, b, c

// Suppression des relations multiples
MATCH (a)-[r]->(b)
WITH a, b, r
ORDER BY r.Num_Acc DESC
WITH a, b, collect(r)[1..] as rels
UNWIND rels as r
DELETE r

// Vue d'ensemble des relations
CALL db.schema.visualization();


// Accident ayant impliqué le plus de véhicules et de victimes
MATCH (n)
RETURN n, size([(n)-[r]->() | r]) as degree
ORDER BY degree DESC
LIMIT 1;

// L'accident ayant le plus de victime 
MATCH (u:Usager)-[r]->(a:Accident)
WITH a, count(r) as degree
RETURN a, degree
ORDER BY degree DESC
LIMIT 1;

// Accident ayant impliqué le plus de véhicules
MATCH (a:Accident)-[r]->(v:Vehicules)
WITH a, count(r) as degree
RETURN a, degree
ORDER BY degree DESC
LIMIT 1;

// Pour rechercher tous les accident autour d'un point 
// remplacer les latitude et longitude de la première ligne par celles du point d'intérêt
WITH point({latitude: 48.8582532, longitude: 2.294287}) AS eiffel
MATCH (a:Accident)
WHERE a.Latitude IS NOT NULL AND a.Longitude IS NOT NULL
WITH a, point.distance(point({latitude: a.Latitude, longitude: a.Longitude}), eiffel) AS distance
WHERE distance < 500
RETURN a.Adresse_postale, distance
ORDER BY distance
LIMIT 100;


// Si les données comportent des adresses sans les coordonnées GPS on les créé avec cette fonction
MATCH (a:Accident)
WHERE a.Adresse_postale IS NOT NULL AND a.Latitude IS NULL
WITH a LIMIT 1000
CALL apoc.spatial.geocodeOnce(a.Adresse_postale) YIELD location
SET a.Latitude = location.latitude
SET a.Longitude = location.longitude;


// Les 5 départements les plus accidentogène
MATCH (a:Accident) RETURN a.`Département`, count(*) as nb ORDER BY nb DESC LIMIT 5


//Classement des fréquences d'accident par année et mois entre 2019 et 2020 
MATCH (n:Accident) 
RETURN n.An as Annee,n.Mois AS mois, COUNT (*) AS nombre_accident 
ORDER BY nombre_accident DESC

//Classement des fréquences d'accident par année et mois entre 2019 et 2020 en fonction du nombre de personnes impliquées et de leur état
MATCH (u:Usager)-[r:EST_CONCERNE]->(a:Accident)
RETURN ToInteger(a.An) AS Annee,ToInteger(a.Mois) AS mois, 
    COUNT (distinct(a.Num_Acc)) AS nombre_accident , 
    COUNT (a.Num_Acc)AS nombre_personne_impliqué,
    SUM(CASE WHEN(u.grav="1") THEN 1 ELSE 0 END) AS dont_indemne,
    SUM(CASE WHEN(u.grav="2") THEN 1 ELSE 0 END) AS dont_décédée,
    SUM(CASE WHEN(u.grav="3") THEN 1 ELSE 0 END) AS dont_hospitalisé,
    SUM(CASE WHEN(u.grav="4") THEN 1 ELSE 0 END) AS dont_blessé_léger,
    SUM(CASE WHEN(u.grav=" -1") THEN 1 ELSE 0 END) AS non_renseigné
ORDER BY nombre_accident DESC


//Profil Conducteur les plus à risque
MATCH (u:Usager)-[r:EST_CONCERNE]->(a:Accident) 
WHERE a.An IS NOT NULL // à modifier si 
AND  u.an_nais IS NOT NULL 
AND u.catu = "1" 
    RETURN  CASE WHEN u.sexe="1" THEN"Homme"
        ELSE CASE WHEN u.sexe="2" THEN "Femme" ELSE "non renseigné" END 
        END AS sexe, 
        (ToInteger(a.An)-Tointeger(u.an_nais)) AS Age,
        COUNT(*) AS nb_accident 
        ORDER BY nb_accident DESC


//lieux des accidents en fonction des catégories de route sur les 5 départements en Hauts-de-France : Aisne (02),Nord (59),Oise (60),Pas-de-Calais (62),Somme (80)
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


// répartition mensuelle des accidents en fonction des condidtions météorologique
MATCH (a:Accident)
WHERE a.Mois IS NOT NULL AND  a.`Conditions_atmosphériques`IS NOT NULL

WITH a.`Conditions_atmosphériques` AS Meteo, a.Mois AS M, COUNT(a.Num_Acc) AS nb
WITH Meteo, apoc.map.fromLists(COLLECT(M), COLLECT(nb)) AS piv
RETURN CASE Meteo 
WHEN "1" THEN "Normale" 
      WHEN "2" THEN "Pluie_legere" 
         WHEN "3" THEN "Pluie_forte"
             WHEN "4" THEN "Neige_grele"
                 WHEN  "5" THEN "Brouillard_fumee"
                     WHEN "6" THEN "Vent_fort_tempete"
                         WHEN "7" THEN "Temps_eblouissant"
					WHEN "8" THEN "Temps_couvert"
                         		WHEN "9" THEN "Autre" 
							WHEN " -1" THEN "non renseignée" end as Meteo ,
  piv["01"] AS Janv,
  piv["02"] AS Fev,
  piv["03"] AS Mars,
  piv["04"] AS Avr,
  piv["05"] AS Mai,
  piv["06"] AS Juin,
  piv["07"] AS Juill,
  piv["08"] AS Aout,
  piv["09"] AS Sept,
  piv["10"] AS Oct,
  piv["11"] AS Nov,
  piv["12"] AS Dec

// visualisation des pietons décédés lors d'un accident impliquant 1 ou plusieurs véhicule

MATCH(u:Usager {catu:"3",grav:"2"})-[r:EST_PRESENT]->(v:Vehicules)
return u,r,v

// répartition annuelle des accidents en fonction de l'éclairage et de localisation


MATCH (a:Accident)
WHERE a.An IS NOT NULL 

WITH a.`Lumière`AS e , a.Localisation AS l,a.An AS A, COUNT(a.Num_Acc) AS nb
WITH e,l, apoc.map.fromLists(COLLECT(A), COLLECT(nb)) AS piv
RETURN 

CASE l 
WHEN "1" THEN "Hors agglomération " 
      WHEN "2" THEN "En agglomération " end as Localisalion,
CASE e 
WHEN "1" THEN "Plein jour" 
      WHEN "2" THEN "Crépuscule ou aube" 
         WHEN "3" THEN "Nuit sans éclairage public"
             WHEN "4" THEN "Nuit avec éclairage public non allumé"
                 WHEN  "5" THEN "Nuit avec éclairage public allumée"
                     WHEN " -1" THEN "non renseignée" end as Eclairage ,

  piv["2019"] AS An_2019,
  piv["2020"] AS An_2020,
  piv["2021"] AS An_2021
      
ORDER BY Localisalion,Eclairage

// visualiser les accidents impliquant jusqu'à 6 véhicules
MATCH(a:Accident)-[r:IMPLIQUE*1..6]->(v:Vehicules)
return a,v

//Visualiser les accidents impliquant 3 véhicules et plus et dont l'un deux est un vélo
WITH ["4", "5"] as col
MATCH (a:Accident)
WHERE ANY (i IN col WHERE i = a.Type_de_collision )


MATCH (l:Lieux )<-[r2:EST_LOCALISE]-(a: Accident)<-[r:EST_CONCERNE]-(u:Usager)
WHERE a.An='2021'  AND l.Categorie="1" AND u.grav="3"
RETURN a.Latitude AS Latitude ,a.Longitude AS longitude