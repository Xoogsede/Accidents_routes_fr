Lumiere = {
	"Plein_jour":1,
	"Crepuscule_ou_aube":2,
	"Nuit_sans_eclairage_public":3,
	"Nuit_avec_eclairage_public_non_allume":4,
	"Nuit_avec_eclairage_public_allume":5}


Localisation = {
	"Hors_agglomeration":1,
	"En_agglomeration":2}

Intersection = {
	"Hors_intersection":1,
	"Intersection_en_X":2,
	"Intersection_en_T":3,
	"Intersection_en_Y":4,
	"Intersection_a_plus_de_4_branches":5,
	"Giratoire":6,
	"Place":7,
	"Passage_a_niveau":8,
	"Autre_intersection":9}

Conditions_atm = {
    "Non_renseigne":-1,
	"Normale":1,
	"Pluie_legere":2,
	"Pluie_forte":3,
	"Neige_grele":4,
	"Brouillard_fumee":5,
	"Vent_fort_tempete":6,
	"Temps_eblouissant":7,
	"Temps_couvert":8,
	"Autre":9}

Type_de_collision =  {
	"Non_renseigne":-1,
	"Deux_vehicules_frontale":1,
	"Deux_vehicules_par_arriere":2,
	"Deux_vehicules_par_le_cote":3,
	"Trois_vehicules_et_plus_en_chaine":4,
	"Trois_vehicules_et_plus_collisions_multiple":5,
	"Autre_collision":6,
	"Sans_collision":7}

#Lieux

Categorie_de_route =  {
	"Autoroute":1,
	"Route_nationale":2,
	"Route_Departementale":3,
	"Voie_Communales":4,
	"Hors_reseau_public":5,
	"Parc_de_stationnement_ouvert_a_la_circulation_publique":6,
	"Routes_de_metropole_urbaine":7,
	"autre__voie__Numero_de_la_route.":9}

Regime_de_circulation =  {
	"Non_renseigne":-1,
	"A_sens_unique":1,
	"Bidirectionnelle":2,
	"A_chaussees_séparees":3,
	"Avec_voies_d’affectation_variable":4}

Voie_reservee =  {
	"Non_renseigne":-1,
	"Sans_objet":0,
	"Piste_cyclable":1,
	"Bande_cyclable":2,
	"Voie_reservee":3}

Profil_route=  {
	"Non_renseigne":-1,
	"Plat":1,
	"Pente":2,
	"Sommet_de_cote":3,
	"Bas_de_cote":4}

Trace_plan=  {
	"Non_renseigne":-1,
	"Partie_rectiligne":1,
	"En_courbe_a_gauche":2,
	"En_courbe_a_droite":3,
	"En_«_S_»":4}


Etat_surface=  {
	"Non_renseigne":-1,
	"Normale":1,
	"Mouillee":2,
	"Flaques":3,
	"Inondee":4,
	"Enneigee":5,
	"Boue":6,
	"Verglacee":7,
	"Corps_gras_–_huile":8,
	"Autre":9}

Amenagement_Infrastructure=  {
	"Non_renseigne":-1,
	"Aucun":0,
	"Souterrain_tunnel":1,
	"Pont_autopont":2,
	"Bretelle_d_echangeur_ou_de_raccordement":3,
	"Voie_ferree":4,
	"Carrefour_amenage":5,
	"Zone_pietonne":6,
	"Zone_de_peage":7,
	"Chantier":8,
	"Autres":9}

Situation_accident=  {
	"Non_renseigne":-1,
	"Aucun":0,
	"Sur_chaussee":1,
	"Sur_bande_d_arret_d_urgence":2,
	"Sur_accotement":3,
	"Sur_trottoir":4,
	"Sur_piste_cyclable":5,
	"Sur_autre_voie_speciale":6,
	"Autres":8}


# vehicule 

Sens_circulation=  {
	-1: 'Non renseigné',
	0: 'Inconnu',
	1: 'PK ou PR ou numéro d’adresse postale croissant',
	2: 'PK ou PR ou numéro d’adresse postale décroissant',
	3: 'Absence de repère'}


Catégorie_du_véhicule = {
	0: 'Indéterminable',
	1: 'Bicyclette',
	2: 'Cyclomoteur <50cm3',
	3: 'Voiturette (Quadricycle à moteur carrossé) (anciennement "voiturette ou tricycle à moteur")',
	4: 'Référence inutilisée depuis 2006 (scooter immatriculé)',
	5: 'Référence inutilisée depuis 2006 (motocyclette)',
	6: 'Référence inutilisée depuis 2006 (side-car)',
	7: 'VL seul',
	8: 'Référence inutilisée depuis 2006 (VL + caravane)',
	9: 'Référence inutilisée depuis 2006 (VL + remorque)',
	10: 'VU seul 1,5T <= PTAC <= 3,5T avec ou sans remorque (anciennement VU seul 1,5T <= PTAC <= 3,5T)',
	11: 'Référence inutilisée depuis 2006 (VU (10) + caravane)',
	12: 'Référence inutilisée depuis 2006 (VU (10) + remorque)',
	13: 'PL seul 3,5T <PTCA <= 7,5T',
	14: 'PL seul > 7,5T',
	15: 'PL > 3,5T + remorque',
	16: 'Tracteur routier seul',
	17: 'Tracteur routier + semi-remorque',
	18: 'Référence inutilisée depuis 2006 (transport en commun)',
	19: 'Référence inutilisée depuis 2006 (tramway)',
	20: 'Engin spécial',
	21: 'Tracteur agricole',
	30: 'Scooter < 50 cm3',
	31: 'Motocyclette > 50 cm3 et <= 125 cm3 ',
	32: 'Scooter > 50 cm3 et <= 125 cm3 ',
	33: 'Motocyclette > 125 cm3 ',
	34: 'Scooter > 125 cm3 ',
	35: 'Quad léger <= 50 cm3 (Quadricycle à moteur non carrossé)',
	36: 'Quad lourd > 50 cm3 (Quadricycle à moteur non carrossé)',
	37: 'Autobus',
	38: 'Autocar',
	39: 'Train ',
	40: 'Tramway',
	41: '3RM <= 50 cm3',
	42: '3RM > 50 cm3 <= 125 cm3',
	43: '3RM > 125 cm3',
	50: 'EDP à moteur',
	60: 'EDP sans moteur',
	80: 'VAE',
	99: 'Autre véhicule'}

Obstacle_fixe_heurte = {
	-1: 'Non renseigné',
	0: 'Sans objet',
	1: 'Véhicule en stationnement',
	2: 'Arbre',
	3: 'Glissière métallique',
	4: 'Glissière béton',
	5: 'Autre glissière',
	6: 'Bâtiment, mur, pile de pont',
	7: 'Support de signalisation verticale ou poste d’appel d’urgence',
	8: 'Poteau',
	9: 'Mobilier urbain',
	10: 'Parapet',
	11: 'Ilot, refuge, borne haute',
	12: 'Bordure de trottoir',
	13: 'Fossé, talus, paroi rocheuse',
	14: 'Autre obstacle fixe sur chaussée',
	15: 'Autre obstacle fixe sur trottoir ou accotement',
	16: 'Sortie de chaussée sans obstacle',
	17: 'Buse – tête d’aqueduc'}

Obstacle_mobile_heurte = {
	-1: 'Non renseigné',
	0: 'Aucun',
	1: 'Piéton',
	2: 'Véhicule',
	4: 'Véhicule sur rail',
	5: 'Animal domestique',
	6: 'Animal sauvage',
	9: 'Autre'}

Point_choc_initial = {
	-1: 'Non renseigné',
	0: 'Aucun',
	1: 'Avant',
	2: 'Avant droit',
	3: 'Avant gauche',
	4: 'Arrière',
	5: 'Arrière droit',
	6: 'Arrière gauche',
	7: 'Côté droit',
	8: 'Côté gauche',
	9: 'Chocs multiples (tonneaux)'}

Manoeuvre_principale_avant_accident = {
	-1: 'Non renseigné',
	0: 'Inconnue',
	1: 'Sans changement de direction',
	2: 'Même sens, même file',
	3: 'Entre 2 files',
	4: 'En marche arrière',
	5: 'A contresens',
	6: 'En franchissant le terre-plein central',
	7: 'Dans le couloir bus, dans le même sens',
	8: 'Dans le couloir bus, dans le sens inverse',
	9: 'En s’insérant',
	10: 'En faisant demi-tour sur la chaussée',
 	11: 'Changeant de file à gauche',
	12: 'Changeant de file à droite',
	13: 'Déporté à gauche',
	14: 'Déporté à  droite',
	15: 'Tournant à gauche',
	16: 'Tournant à droite',
	17: 'Dépassant à gauche',
	18: 'Dépassant à droite',
	19: 'Traversant la chaussée',
	20: 'Manœuvre de stationnement',
	21: 'Manœuvre d’évitement',
	22: 'Ouverture de porte',
	23: 'Arrêté (hors stationnement)',
	24: 'En stationnement (avec occupants)',
	25: 'Circulant sur trottoir',
	26: 'Autres manœuvres'}

Type_motorisation_vehicule = {
	-1: 'Non renseigné',
	0: 'Inconnue',
	1: 'Hydrocarbures',
	2: 'Hybride électrique',
	3: 'Electrique',
	4: 'Hydrogène',
	5: 'Humaine',
	6: 'Autre'}

#usager

Categorie_usager = {
	-1: 'Non renseigné',
	'Conducteur':1,
	'Passager':2,
	'Piéton':3}
Gravite_blessure_usager = {
	
	1: 'Indemne',
	2: 'Tué',
	3: 'Blessé hospitalisé',
	4: 'Blessé léger'}

Sexe_usager = {
	-1: 'Non renseigné',
	1: 'Masculin',
	2: 'Féminin'}

Motif_deplacement_lors_accident = {
	-1: 'Non renseigné',
	0: 'Non renseigné',
	1: 'Domicile-travail',
	2: 'Domicile-école',
	3: 'Courses-achats',
	4: 'Utilisation professionnelle',
	5: 'Promenade-loisirs',
	9: 'Autre'}

Securite1_usager = {
	-1: 'Non renseigné',
	0: 'Aucun équipement',
	1: 'Ceinture',
	2: 'Casque',
	3: 'Dispositif enfants',
	4: 'Gilet réfléchissant',
	5: 'Airbag (2RM/3RM)',
	6: 'Gants (2RM/3RM)',
	7: 'Gants + Airbag (2RM/3RM)',
	8: 'Non déterminable',
	9: 'Autre'}

Securite2_usager = {
	-1: 'Non renseigné',
	0: 'Aucun équipement',
	1: 'Ceinture',
	2: 'Casque',
	3: 'Dispositif enfants',
	4: 'Gilet réfléchissant',
	5: 'Airbag (2RM/3RM)',
	6: 'Gants (2RM/3RM)',
	7: 'Gants + Airbag (2RM/3RM)',
	8: 'Non déterminable',
	9: 'Autre'}

Securite3_usager = {
	-1: 'Non renseigné',
	0: 'Aucun équipement',
	1: 'Ceinture',
	2: 'Casque',
	3: 'Dispositif enfants',
	4: 'Gilet réfléchissant',
	5: 'Airbag (2RM/3RM)',
	6: 'Gants (2RM/3RM)',
	7: 'Gants + Airbag (2RM/3RM)',
	8: 'Non déterminable',
	9: 'Autre'}

Localisation_pieton = {
	-1: 'Non renseigné',
	0: 'Sans objet',
	1: 'Sur chaussée à + 50 m du passage piéton',
	2: 'Sur chaussée à - 50 m du passage piéton',
	3: 'Sur passage piéton sans signalisation lumineuse',
	4: 'Sur passage piéton avec signalisation lumineuse',
	5: 'Sur trottoir',
	6: 'Sur accotement',
	7: 'Sur refuge ou BAU',
	8: 'Sur contre allée',
	9: 'Inconnue'}

Action_pieton = {
	-1: 'Non renseigné',   
	0: 'Non renseigné ou sans objet',  
	1: 'Se déplaçant dans le sens véhicule heurtant',  
	2: 'Se déplaçant dans le sens inverse du véhicule',  
	3: 'Traversant',  
	4: 'Masqué',   
	5: 'Jouant - courant',  
	6: 'Avec animal',  
	9: 'Autre',  
	'A': 'Monte/descend du véhicule',  
	'B': 'Inconnue'}  

Etat_pieton = { 
	-1: 'Non renseigné',   
	1: 'Seul',  
	2: 'Accompagné',  
	3: 'En groupe'}


# funcion qui permet de s'assurer que les clés des dictionnaire sont bien les integer
# utilisé dans le tableau 
def dic_convert(dictionnaire):
	for k, v in dictionnaire.items():				
		new_dict = {}
		if (type(k) == 'int' or len(str(k)) == 1):
			new_dict[v]=k			
		else:
			new_dict = dictionnaire
	
	return new_dict
