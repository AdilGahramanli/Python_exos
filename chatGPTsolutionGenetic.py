import folium
import math
import random

def distance_entre_villes(ville1, ville2):
    # Calculer la distance euclidienne entre deux villes à partir de leurs coordonnées GPS
    lat1, lon1 = ville1
    lat2, lon2 = ville2
    return math.sqrt((lat2 - lat1)**2 + (lon2 - lon1)**2)

def algorithme_glouton(villes, ville_depart):
    chemin = [ville_depart]
    villes_non_visitees = list(villes.keys())
    villes_non_visitees.remove(ville_depart)

    while villes_non_visitees:
        ville_actuelle = chemin[-1]
        ville_suivante = min(villes_non_visitees, key=lambda ville: distance_entre_villes(villes[ville_actuelle], villes[ville]))
        chemin.append(ville_suivante)
        villes_non_visitees.remove(ville_suivante)

    return chemin

def evaluer_trajet(trajet, villes):
    distance_totale = 0
    for i in range(len(trajet) - 1):
        distance_totale += distance_entre_villes(villes[trajet[i]], villes[trajet[i+1]])
    distance_totale += distance_entre_villes(villes[trajet[-1]], villes[trajet[0]])
    return distance_totale

def selection_roulette(population, villes):
    total_fitness = sum(1 / evaluer_trajet(trajet, villes) for trajet in population)
    roulette_wheel = []
    current_fitness = 0
    for trajet in population:
        current_fitness += (1 / evaluer_trajet(trajet, villes)) / total_fitness
        roulette_wheel.append((current_fitness, trajet))
    selected = []
    for _ in range(len(population)):
        r = random.random()
        for index, (fitness, trajet) in enumerate(roulette_wheel):
            if r <= fitness:
                selected.append(trajet)
                break
    return selected

def crossover(parent1, parent2):
    start_index = random.randint(0, len(parent1) - 1)
    end_index = random.randint(start_index, len(parent1) - 1)
    child = [None] * len(parent1)
    for i in range(start_index, end_index + 1):
        child[i] = parent1[i]
    remaining_cities = [city for city in parent2 if city not in child]
    j = 0
    for i in range(len(parent1)):
        if child[i] is None:
            child[i] = remaining_cities[j]
            j += 1
    return child

def mutation(trajet, mutation_rate):
    if random.random() < mutation_rate:
        index1 = random.randint(0, len(trajet) - 1)
        index2 = random.randint(0, len(trajet) - 1)
        trajet[index1], trajet[index2] = trajet[index2], trajet[index1]

def algorithme_genetique(villes, population_initiale, generations, mutation_rate):
    population = population_initiale[:]
    for _ in range(generations):
        population = selection_roulette(population, villes)
        new_population = []
        while len(new_population) < len(population_initiale):
            parent1 = random.choice(population)
            parent2 = random.choice(population)
            child = crossover(parent1, parent2)
            mutation(child, mutation_rate)
            new_population.append(child)
        population = new_population
        print(distance_totale_parcourue(min(population, key=lambda trajet: evaluer_trajet(trajet, villes))))
    meilleur_trajet = min(population, key=lambda trajet: evaluer_trajet(trajet, villes))
    return meilleur_trajet

#Calcul des distances entre les villes

def distance_totale_parcourue(villes, trajet):
    """
    Calcule la distance totale parcourue lorsqu'on traverse toutes les villes dans l'ordre spécifié.

    Args:
        villes (dict): Dictionnaire contenant les coordonnées GPS de chaque ville.
                       Clé: nom de la ville
                       Valeur: tuple (latitude, longitude)
        trajet (list): Liste ordonnée des noms des villes à visiter.

    Returns:
        float: Distance totale parcourue pour parcourir toutes les villes dans l'ordre spécifié.
    """
    distance_totale = 0
    for i in range(len(trajet) - 1):
        ville_actuelle = trajet[i]
        ville_suivante = trajet[i + 1]
        if ville_actuelle in villes and ville_suivante in villes:
            distance_totale += distance_entre_villes(villes[ville_actuelle], villes[ville_suivante])
        else:
            print(f"Erreur: Ville manquante dans le dictionnaire de villes: {ville_actuelle} ou {ville_suivante}")
    if trajet[-1] in villes and trajet[0] in villes:  # Ajout d'une vérification pour le dernier trajet de retour
        distance_totale += distance_entre_villes(villes[trajet[-1]], villes[trajet[0]])
    else:
        print("Erreur: Ville manquante dans le dictionnaire de villes pour le dernier trajet de retour.")
    return distance_totale




# Coordonnées GPS des 70 villes autour de Grenoble
villes_autour_grenoble = {
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

# Générer une population initiale de 20 trajets en utilisant l'algorithme glouton
population_initiale = [algorithme_glouton(villes_autour_grenoble, "Ville 1") for _ in range(100)]

# Appliquer l'algorithme génétique pour optimiser la population initiale
meilleur_trajet = algorithme_genetique(villes_autour_grenoble, population_initiale, generations=1000, mutation_rate=0.1)

# Créer une carte centrée sur Grenoble
ma_carte = folium.Map(location=[45.1885, 5.7245], zoom_start=10)

# Ajouter un marqueur pour chaque ville
for ville, coordonnees in villes_autour_grenoble.items():
    folium.Marker(location=coordonnees, popup=ville).add_to(ma_carte)

# Ajouter les lignes du trajet optimal
chemin_meilleur_trajet = [villes_autour_grenoble[ville] for ville in meilleur_trajet]

score=distance_totale_parcourue(villes_autour_grenoble,chemin_meilleur_trajet)
print (score)

folium.PolyLine(locations=chemin_meilleur_trajet, color='blue', weight=5).add_to(ma_carte)

# Afficher la carte
ma_carte.save("trajet_optimal_autour_de_grenoble.html")
