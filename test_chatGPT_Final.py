import folium
import random
import math

# Coordonnées des villes
coordonnees_villes = [
    (45.985963301267475, 5.879349146969616), (45.95404105819762, 5.958502317313105), (45.872244850732386, 5.968522221781313),
    (45.8415000801906, 5.959904422052205), (45.79845806863159, 5.951424847822636), (45.79241708293557, 5.944928959477693),
    (45.76284674461931, 5.927439529914409), (45.8281201608479, 5.897455509752035), (45.653926549013704, 5.874122806359082),
    (45.70067735388875, 5.664661933667958), (45.760046638548374, 5.626114178448915), (45.809219979681075, 5.6553536048159),
    (45.86296355910599, 5.607678048778325), (45.83378930576146, 5.594218102283776), (45.778126823715866, 5.496823584660888),
    (45.786116554401815, 5.383716525975615), (45.86593687767163, 5.447151481173933), (45.87016374338418, 5.329219799023122),
    (45.96130276285112, 5.20931842783466), (45.977971160784364, 5.075682507827878), (45.842319757677615, 5.00712564913556),
    (45.913451181259006, 5.140393556561321), (45.885941847227514, 5.218129512388259), (45.73678634874523, 5.244391959160566),
    (45.71515649650246, 5.155064743477851), (45.64814301766455, 5.13183926558122), (45.6225799061358, 5.166868498083204),
    (45.65203353576362, 5.100120427086949), (45.61406330252066, 5.026568689849228), (45.59234014619142, 5.012781799770892),
    (45.511859357822686, 5.044355486985296), (45.4749185196124, 5.033659254200757), (45.45252101030201, 5.030553195159882),
    (45.333723647054285, 5.04573412053287), (45.49334197444841, 5.160002375487238), (45.5387847404927, 5.299034046474844),
    (45.46118817990646, 5.289059322793037), (45.38558286521584, 5.354603902902454), (45.3535090405494, 5.320941847283393),
    (45.22311807330698, 5.216796220745891), (45.19039539759979, 5.203853769227862), (45.176194752566516, 5.253388612996787),
    (45.15391706256196, 5.261083357501775), (45.18163343332708, 5.28235941613093), (45.16840846976265, 5.318457887973636),
    (45.2075217734091, 5.338951533194631), (45.189740660600364, 5.360775381792337), (45.22666524536908, 5.450072779785842),
    (45.245897417888045, 5.541917126160115), (45.1144593548961, 5.33731721714139), (45.001877955626696, 5.417060643434525),
    (45.04060538858175, 5.532846525777131), (45.08402152825147, 5.589844330679625), (45.06421244936064, 5.716887802816927),
    (45.037849066313356, 5.906032455619425), (45.21194481430575, 5.945849186740816), (45.169246106408536, 5.741571342106909),
    (45.24255100591108, 5.662926422432065), (45.477704676799476, 5.931255214847624), (45.53482529288158, 5.828228288330138),
    (45.46834090864286, 5.815425308421254), (45.494997459463775, 5.708030846901238), (45.47372017102316, 5.580604142975062),
    (45.43971620267257, 5.504584172740579), (45.41219567274675, 5.480000180657953), (45.429842443205416, 5.487715854775161),
    (45.44755924260244, 5.492616587784141), (45.578904894180596, 5.600551066920161), (45.60677845263854, 5.374822916928679),
    (45.569365015253425, 5.473787421826273)
]

# Fonction pour calculer la distance entre deux villes à partir de leurs coordonnées GPS
def distance_entre_villes(ville1, ville2):
    lat1, lon1 = ville1
    lat2, lon2 = ville2
    return math.sqrt((lat2 - lat1) ** 2 + (lon2 - lon1) ** 2)

# Fonction pour calculer la distance totale parcourue pour un trajet
def distance_totale_parcourue(trajet):
    distance_totale = 0
    for i in range(len(trajet) - 1):
        ville_actuelle = trajet[i]
        ville_suivante = trajet[i + 1]
        distance_totale += distance_entre_villes(ville_actuelle, ville_suivante)
    return distance_totale

# Fonction pour générer une population initiale de trajets
def generer_population_initiale(coordonnees_villes, taille_population):
    population_initiale = []
    for _ in range(taille_population):
        trajet = coordonnees_villes.copy()
        random.shuffle(trajet)
        population_initiale.append(trajet)
    return population_initiale

# Algorithme génétique pour résoudre le problème du voyageur de commerce
def algorithme_genetique(coordonnees_villes, taille_population, iterations):
    population = generer_population_initiale(coordonnees_villes, taille_population)
    meilleur_trajet = min(population, key=distance_totale_parcourue)
    meilleur_distance = distance_totale_parcourue(meilleur_trajet)
    
    for i in range(iterations):
        nouvelle_population = []
        for _ in range(taille_population):
            parent1, parent2 = random.choices(population, k=2)
            point_de_croisement = random.randint(0, len(coordonnees_villes) - 1)
            enfant = parent1[:point_de_croisement] + [ville for ville in parent2 if ville not in parent1[:point_de_croisement]]
            nouvelle_population.append(enfant)
        population = nouvelle_population
        
        meilleur_trajet_actuel = min(population, key=distance_totale_parcourue)
        meilleure_distance_actuelle = distance_totale_parcourue(meilleur_trajet_actuel)
        
        if meilleure_distance_actuelle < meilleur_distance:
            meilleur_trajet = meilleur_trajet_actuel
            meilleur_distance = meilleure_distance_actuelle
    
    return meilleur_trajet

# Affichage du trajet sur une carte Folium
def afficher_trajet_sur_carte(coordonnees_villes, trajet):
    carte = folium.Map(location=[45.5, 5.5], zoom_start=8)

    # Ajout des marqueurs pour chaque ville
    for index, coordonnees in enumerate(coordonnees_villes):
        folium.Marker(coordonnees, tooltip=str(index)).add_to(carte)

    ligne_trajet=[]
    # Ajout de la ligne représentant le trajet
    for i in range(0,len(trajet)):
        ligne_trajet.append(coordonnees_villes[i])
    # ligne_trajet = [coordonnees_villes[i] for i in trajet] + [coordonnees_villes[trajet[0]]]
    folium.PolyLine(locations=ligne_trajet, color='blue').add_to(carte)

    carte.save('carte_trajet.html')

# Paramètres de l'algorithme génétique
TAILLE_POPULATION = 100
ITERATIONS = 1000

# Exécution de l'algorithme génétique
meilleur_trajet = algorithme_genetique(coordonnees_villes, TAILLE_POPULATION, ITERATIONS)

# Affichage du trajet sur une carte Folium
afficher_trajet_sur_carte(coordonnees_villes, meilleur_trajet)

print("Trajet le plus court trouvé:", meilleur_trajet)
print("Distance totale parcourue:", distance_totale_parcourue(meilleur_trajet))
