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


# Rayon de la Terre en mètres
RAYON_TERRE = 6371

# Convertir les coordonnées de degrés en radians
def degres_vers_radians(degres):
    return degres * math.pi / 180

# Calculer la distance entre deux points géographiques en utilisant la formule de l'Haversine
def distance_haversine(coord1, coord2):
    lat1, lon1 = coord1
    lat2, lon2 = coord2

    d_lat = degres_vers_radians(lat2 - lat1)
    d_lon = degres_vers_radians(lon2 - lon1)

    a = math.sin(d_lat / 2) ** 2 + math.cos(degres_vers_radians(lat1)) * math.cos(degres_vers_radians(lat2)) * math.sin(d_lon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = RAYON_TERRE * c

    return distance

# Exemple d'utilisation
# ville1 = (45.985963301267475, 5.879349146969616)
# ville2 = (45.95404105819762, 5.958502317313105)
# distance = distance_haversine(ville1, ville2)
# print("Distance entre les deux villes :", distance, "mètres")

# Fonction pour calculer la distance entre deux villes à partir de leurs coordonnées GPS
def distance_entre_villes(ville1, ville2):
    # lat1, lon1 = ville1
    # lat2, lon2 = ville2
    # return math.sqrt((lat2 - lat1) ** 2 + (lon2 - lon1) ** 2)
    return distance_haversine(ville1,ville2)

# Fonction pour calculer la distance totale parcourue pour un trajet
def distance_totale_parcourue(trajet):
    distance_totale = 0
    for i in range(len(trajet) - 1):
        ville_actuelle = trajet[i]
        ville_suivante = trajet[i + 1]
        distance_totale += distance_entre_villes(ville_actuelle, ville_suivante)
    return distance_totale

# Algorithme glouton pour trouver un trajet initial
def algorithme_glouton(coordonnees_villes):
    trajet = []
    villes_restantes = coordonnees_villes.copy()
    ville_depart = villes_restantes.pop(0)
    trajet.append(ville_depart)
    while villes_restantes:
        prochaine_ville = min(villes_restantes, key=lambda ville: distance_entre_villes(trajet[-1], ville))
        trajet.append(prochaine_ville)
        villes_restantes.remove(prochaine_ville)
    return trajet

# Génération de la population initiale en utilisant l'algorithme glouton
population_initiale = [algorithme_glouton(coordonnees_villes) for _ in range(30)]

# Affichage de la population initiale (juste pour vérification)
print("Population initiale générée avec l'algorithme glouton:")
for trajet in population_initiale:
    print(trajet)
    print("Distance totale parcourue:", distance_totale_parcourue(trajet))

# Affichage du premier trajet sur une carte Folium
def afficher_trajet_sur_carte(coordonnees_villes, trajet):
    carte = folium.Map(location=[45.5, 5.5], zoom_start=8)

    # Ajout des marqueurs pour chaque ville
    for index, coordonnees in enumerate(coordonnees_villes):
        folium.Marker(coordonnees, tooltip=str(index)).add_to(carte)

    # # Ajout de la ligne représentant le trajet
    # ligne_trajet = [coordonnees_villes[i] for i in trajet] + [coordonnees_villes[trajet[0]]]
    ligne_trajet=[]
    # Ajout de la ligne représentant le trajet
    for i in range(0,len(trajet)):
        ligne_trajet.append(coordonnees_villes[i])
    folium.PolyLine(locations=ligne_trajet, color='red').add_to(carte)

    carte.save('carte_trajet.html')

# Affichage du premier trajet sur une carte Folium
afficher_trajet_sur_carte(coordonnees_villes, population_initiale[0])
