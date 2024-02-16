import  folium
import  math


# Coordonnées des 70 villes
villes = {
    "Ville 1": (45.985963301267475, 5.879349146969616),
    "Ville 2": (45.95404105819762, 5.958502317313105),
    "Ville 3": (45.872244850732386, 5.968522221781313),
    "Ville 4": (45.8415000801906, 5.959904422052205),
    "Ville 5": (45.79845806863159, 5.951424847822636),
    "Ville 6": (45.79241708293557, 5.944928959477693),
    "Ville 7": (45.76284674461931, 5.927439529914409),
    "Ville 8": (45.8281201608479, 5.897455509752035),
    "Ville 9": (45.653926549013704, 5.874122806359082),
    "Ville 10": (45.70067735388875, 5.664661933667958),
    "Ville 11": (45.760046638548374, 5.626114178448915),
    "Ville 12": (45.809219979681075, 5.6553536048159),
    "Ville 13": (45.86296355910599, 5.607678048778325),
    "Ville 14": (45.83378930576146, 5.594218102283776),
    "Ville 15": (45.778126823715866, 5.496823584660888),
    "Ville 16": (45.786116554401815, 5.383716525975615),
    "Ville 17": (45.86593687767163, 5.447151481173933),
    "Ville 18": (45.87016374338418, 5.329219799023122),
    "Ville 19": (45.96130276285112, 5.20931842783466),
    "Ville 20": (45.977971160784364, 5.075682507827878),
    "Ville 21": (45.842319757677615, 5.00712564913556),
    "Ville 22": (45.913451181259006, 5.140393556561321),
    "Ville 23": (45.885941847227514, 5.218129512388259),
    "Ville 24": (45.73678634874523, 5.244391959160566),
    "Ville 25": (45.71515649650246, 5.155064743477851),
    "Ville 26": (45.64814301766455, 5.13183926558122),
    "Ville 27": (45.6225799061358, 5.166868498083204),
    "Ville 28": (45.65203353576362, 5.100120427086949),
    "Ville 29": (45.61406330252066, 5.026568689849228),
    "Ville 30": (45.59234014619142, 5.012781799770892),
    "Ville 31": (45.511859357822686, 5.044355486985296),
    "Ville 32": (45.4749185196124, 5.033659254200757),
    "Ville 33": (45.45252101030201, 5.030553195159882),
    "Ville 34": (45.333723647054285, 5.04573412053287),
    "Ville 35": (45.49334197444841, 5.160002375487238),
    "Ville 36": (45.5387847404927, 5.299034046474844),
    "Ville 37": (45.46118817990646, 5.289059322793037),
    "Ville 38": (45.38558286521584, 5.354603902902454),
    "Ville 39": (45.3535090405494, 5.320941847283393),
    "Ville 40": (45.22311807330698, 5.216796220745891),
    "Ville 41": (45.19039539759979, 5.203853769227862),
    "Ville 42": (45.176194752566516, 5.253388612996787),
    "Ville 43": (45.15391706256196, 5.261083357501775),
    "Ville 44": (45.18163343332708, 5.28235941613093),
    "Ville 45": (45.16840846976265, 5.318457887973636),
    "Ville 46": (45.2075217734091, 5.338951533194631),
    "Ville 47": (45.189740660600364, 5.360775381792337),
    "Ville 48": (45.22666524536908, 5.450072779785842),
    "Ville 49": (45.245897417888045, 5.541917126160115),
    "Ville 50": (45.1144593548961, 5.33731721714139),
    "Ville 51": (45.001877955626696, 5.417060643434525),
    "Ville 52": (45.04060538858175, 5.532846525777131),
    "Ville 53": (45.08402152825147, 5.589844330679625),
    "Ville 54": (45.06421244936064, 5.716887802816927),
    "Ville 55": (45.037849066313356, 5.906032455619425),
    "Ville 56": (45.21194481430575, 5.945849186740816),
    "Ville 57": (45.169246106408536, 5.741571342106909),
    "Ville 58": (45.24255100591108, 5.662926422432065),
    "Ville 59": (45.477704676799476, 5.931255214847624),
    "Ville 60": (45.53482529288158, 5.828228288330138),
    "Ville 61": (45.46834090864286, 5.815425308421254),
    "Ville 62": (45.494997459463775, 5.708030846901238),
    "Ville 63": (45.47372017102316, 5.580604142975062),
    "Ville 64": (45.43971620267257, 5.504584172740579),
    "Ville 65": (45.41219567274675, 5.480000180657953),
    "Ville 66": (45.429842443205416, 5.487715854775161),
    "Ville 67": (45.44755924260244, 5.492616587784141),
    "Ville 68": (45.578904894180596, 5.600551066920161),
    "Ville 69": (45.60677845263854, 5.374822916928679),
    "Ville 70": (45.569365015253425, 5.473787421826273)
}



def distance_entre_villes(ville1, ville2):
    """
    Calcule la distance entre deux villes à partir de leurs coordonnées GPS.

    Args:
        ville1 (tuple): Coordonnées (latitude, longitude) de la première ville.
        ville2 (tuple): Coordonnées (latitude, longitude) de la deuxième ville.

    Returns:
        float: Distance entre les deux villes.
    """
    lat1, lon1 = ville1
    lat2, lon2 = ville2
    return math.sqrt((lat2 - lat1) ** 2 + (lon2 - lon1) ** 2)

def trajet_glouton(villes):
    """
    Trouve le trajet le plus court pour traverser toutes les villes en utilisant un algorithme glouton.

    Args:
        villes (dict): Dictionnaire des coordonnées GPS de chaque ville.

    Returns:
        list: Trajet le plus court pour traverser toutes les villes.
    """
    ville_depart = list(villes.keys())[0]  # Choix arbitraire de la première ville comme ville de départ
    chemin = [ville_depart]
    villes_non_visitees = list(villes.keys())
    villes_non_visitees.remove(ville_depart)

    while villes_non_visitees:
        ville_actuelle = chemin[-1]
        ville_suivante = min(villes_non_visitees, key=lambda ville: distance_entre_villes(villes[ville_actuelle], villes[ville]))
        chemin.append(ville_suivante)
        villes_non_visitees.remove(ville_suivante)

    return chemin


# Fonction pour générer une population de 30 trajets produits par l'algorithme glouton
def generer_population_glouton(villes):
    population = []
    for _ in range(30):
        trajet = trajet_glouton(villes)  # Utilisation de l'algorithme glouton pour générer un trajet
        population.append(trajet)
    return population

# Génération de la population de 30 trajets produits par l'algorithme glouton
population_glouton = generer_population_glouton(villes)

# Affichage de la première solution de la population
print("Première solution de la population générée par l'algorithme glouton :")
print(population_glouton[0])








# Création de la carte
carte = folium.Map(location=[45.5, 5.5], zoom_start=8)

# Ajout des marqueurs pour chaque ville
for ville, coordonnees in villes.items():
    folium.Marker(coordonnees, tooltip=ville).add_to(carte)

# Recherche du trajet optimal
trajet_optimal_glouton = trajet_glouton(villes)

# Ajout des lignes pour représenter le trajet
for i in range(len(trajet_optimal_glouton) - 1):
    ville1 = trajet_optimal_glouton[i]
    ville2 = trajet_optimal_glouton[i + 1]
    folium.PolyLine([villes[ville1], villes[ville2]], color="blue").add_to(carte)

# Affichage de la carte
carte.save("trajet_glouton.html")




import folium

# Fonction pour afficher les villes et les trajets sur une carte Folium
def afficher_carte(villes, trajets):
    # Création de la carte
    carte = folium.Map(location=[45.5, 5.5], zoom_start=8)

    # Ajout des marqueurs pour chaque ville
    for ville, coordonnees in villes.items():
        folium.Marker(coordonnees, tooltip=ville).add_to(carte)

    # Ajout des lignes pour représenter les trajets
    for trajet in trajets:
        for i in range(len(trajet) - 1):
            ville1 = trajet[i]
            ville2 = trajet[i + 1]
            folium.PolyLine([villes[ville1], villes[ville2]], color="blue").add_to(carte)

    # Affichage de la carte
    carte.save("carte_trajets_glouton.html")

# Afficher les villes et les trajets sur la carte
afficher_carte(villes, population_glouton)


import random
import math

# Fonction pour calculer la distance entre deux villes à partir de leurs coordonnées GPS
def distance_entre_villes(ville1, ville2):
    lat1, lon1 = ville1
    lat2, lon2 = ville2
    return math.sqrt((lat2 - lat1) ** 2 + (lon2 - lon1) ** 2)

# Fonction pour calculer la distance totale parcourue pour un trajet
def distance_totale_parcourue(trajet, villes):
    distance_totale = 0
    for i in range(len(trajet) - 1):
        ville_actuelle = trajet[i]
        ville_suivante = trajet[i + 1]
        distance_totale += distance_entre_villes(villes[ville_actuelle], villes[ville_suivante])
    return distance_totale

# Algorithme génétique pour améliorer les trajets
def algorithme_genetique(population, villes, iterations):
    taille_population = len(population)
    
    for _ in range(iterations):
        # Sélection des parents (roue de sélection)
        parents = random.choices(population, weights=[1/distance_totale_parcourue(trajet, villes) for trajet in population], k=taille_population)
        
        # Croisement (crossover)
        enfants = []
        for i in range(0, taille_population, 2):
            parent1 = parents[i]
            parent2 = parents[i+1]
            point_croisement = random.randint(1, len(parent1) - 1)
            enfant1 = parent1[:point_croisement] + [ville for ville in parent2 if ville not in parent1[:point_croisement]]
            enfant2 = parent2[:point_croisement] + [ville for ville in parent1 if ville not in parent2[:point_croisement]]
            enfants.extend([enfant1, enfant2])
        
        # Mutation
        for i in range(len(enfants)):
            if random.random() < 0.05:  # Taux de mutation de 5%
                index1, index2 = random.sample(range(len(enfants[i])), 2)
                enfants[i][index1], enfants[i][index2] = enfants[i][index2], enfants[i][index1]
        
        # Évaluation de la nouvelle population
        population = enfants
    
    # Retourner le meilleur trajet trouvé après les itérations
    return min(population, key=lambda trajet: distance_totale_parcourue(trajet, villes))

# Utilisation de l'algorithme génétique pour améliorer les trajets gloutons
trajet_ameliore = algorithme_genetique(population_glouton, villes, iterations=1000)

# Affichage du trajet amélioré
print("Trajet amélioré:")
print(trajet_ameliore)
print("Distance totale parcourue:", distance_totale_parcourue(trajet_ameliore, villes))


import folium

# Fonction pour afficher les villes et les trajets sur une carte Folium
def afficher_carte_amelioree(villes, trajet_ameliore):
    # Création de la carte
    carte = folium.Map(location=[45.5, 5.5], zoom_start=8)

    # Ajout des marqueurs pour chaque ville
    for ville, coordonnees in villes.items():
        folium.Marker(coordonnees, tooltip=ville).add_to(carte)

    # Ajout des lignes pour représenter le trajet amélioré
    for i in range(len(trajet_ameliore) - 1):
        ville1 = trajet_ameliore[i]
        ville2 = trajet_ameliore[i + 1]
        folium.PolyLine([villes[ville1], villes[ville2]], color="red").add_to(carte)

    # Affichage de la carte
    carte.save("carte_trajet_ameliore.html")

# Afficher les villes et le trajet amélioré sur la carte
afficher_carte_amelioree(villes, trajet_ameliore)

