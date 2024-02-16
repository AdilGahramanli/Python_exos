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
    meilleur_trajet = min(population, key=lambda trajet: evaluer_trajet(trajet, villes))
    return meilleur_trajet

# Coordonnées GPS des 50 villes (à titre d'exemple, des coordonnées aléatoires sont utilisées ici)
villes = {f"Ville {i}": (random.uniform(-90, 90), random.uniform(-180, 180)) for i in range(80)}

# Répéter le processus plusieurs fois pour obtenir le meilleur trajet
meilleur_trajet_global = None
distance_minimale_global = float('inf')
for _ in range(10):  # Répéter 10 fois pour obtenir une meilleure solution
    # Générer une population initiale de 20 trajets en utilisant l'algorithme glouton
    population_initiale = [algorithme_glouton(villes, random.choice(list(villes.keys()))) for _ in range(30)]

    # Appliquer l'algorithme génétique pour optimiser la population initiale
    meilleur_trajet = algorithme_genetique(villes, population_initiale, generations=2000, mutation_rate=0.01)

    # Évaluer le meilleur trajet trouvé
    distance_totale = evaluer_trajet(meilleur_trajet, villes)
    if distance_totale < distance_minimale_global:
        distance_minimale_global = distance_totale
        meilleur_trajet_global = meilleur_trajet

# Créer une carte centrée sur la première ville du meilleur trajet global
ma_carte = folium.Map(location=villes[meilleur_trajet_global[0]], zoom_start=2)

# Ajouter un marqueur pour chaque ville
for ville, coordonnees in villes.items():
    folium.Marker(location=coordonnees, popup=ville).add_to(ma_carte)

# Ajouter le meilleur trajet global sur la carte
chemin_meilleur_trajet_global = [villes[ville] for ville in meilleur_trajet_global]
folium.PolyLine(locations=chemin_meilleur_trajet_global, color='red', weight=2.5, opacity=1).add_to(ma_carte)

# Afficher la carte
ma_carte.save("carte_voyageur_de_commerce_algorithme_genetique_iterations.html")
