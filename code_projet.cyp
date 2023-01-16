//Les paramettre à modifier dans le fichier config:
server.memory.heap.max_size=4096m
dbms.memory.transaction.total.max=104857600000m
db.memory.transaction.max=160000000m

// Chargement des données depuis un fichier CSV "caracteristiques.csv"
LOAD CSV WITH HEADERS FROM 'file:///caracteristiques.csv' AS line FIELDTERMINATOR ";"
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
LOAD CSV WITH HEADERS FROM "file:///lieux.csv" AS row FIELDTERMINATOR ";"
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
LOAD CSV WITH HEADERS FROM "file:///usagers.csv" AS row FIELDTERMINATOR ";"
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


// Chargement des données depuis un fichier CSV "vehicules.csv"
LOAD CSV WITH HEADERS FROM "file:///vehicules.csv" AS row FIELDTERMINATOR ";"
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
CREATE (u)-[:EST_PRESENT]->(v);


// Création de relations entre les nœuds de type "Usager" et "Accident" en utilisant la propriété commune "Num_Acc"
MATCH (u:Usager), (a:Accident)
WHERE u.Num_Acc = a.Num_Acc
  CREATE (u)-[:EST_CONCERNE]->(a);



// Création de relations entre les nœuds de type "Accident" et "Vehicules" en utilisant la propriété commune "Num_Acc"
MATCH (a:Accident), (v:Vehicules)
WHERE a.Num_Acc = v.Num_Acc
  CREATE (a)-[:IMPLIQUE]->(v);


// Création de relations entre les nœuds de type "Accident" et "Lieux" en utilisant la propriété commune "Num_Acc"
MATCH (a:Accident), (l:Lieux)
WHERE a.Num_Acc = l.Num_Acc
  CREATE (a)-[:EST_LOCALISE]->(l);

// Vue d'ensemble des relations
CALL db.schema.visualization()


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


