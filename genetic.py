import  folium
import pandas as pd
import  csv
import  json
import  math
import random


#Les données
class Ville :
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude


m= folium.Map(location=(45.18675902087716, 5.7362964134908285))

listVille = []
with open("Data/70villes.csv", 'r', encoding='UTF-8') as file:
        csvreader = csv.reader(file)
        next(csvreader)  # skip header line
        for row in csvreader:
            ville = Ville(float(row[0]), float(row[1]))
            listVille.append(ville)

####################### CITY NUMBER SETTING
cities_number=20

for i in range(0,cities_number):
    latitude=listVille[i].latitude
    longitude=listVille[i].longitude
    city1=(latitude,longitude)
    cityGrenoble=(45.18675902087716, 5.7362964134908285)
    folium.Marker(
        location=[latitude, longitude],
        tooltip="Click me!",
        popup=(i),
        icon=folium.Icon(icon="cloud",color="blue", icon_color='red',),
        ).add_to(m)
    


##########             Calcul des distances     ########################
def distance_villes(villes,i,j):
    r=6371

    lat_ville1 = villes[i][0]
    long_ville1 = villes[i][1]
    lat_ville2= villes[j][0]
    long_ville2=villes[j][1]

    phi1= lat_ville1 * math.pi/180
    phi2 = lat_ville2*math.pi/180
    deltaPhi = (lat_ville2 - lat_ville1) * math.pi/180
    deltaZegma = (long_ville2 - long_ville1) * math.pi/180

    a=math.sin(deltaPhi/2)*math.sin(deltaPhi/2)+math.cos(phi1)*math.cos(phi2)*math.sin(deltaZegma/2)*math.sin(deltaZegma/2)
    c=2*math.atan2(math.sqrt(a), math.sqrt(1-a))
    d=r*c
    return round(d, 4)


def calculer_distance_total(chemin):
    distance=0
    for i in range(1,len(chemin)):
        distance=distance + distance_villes(chemin,i,i-1)
        
    return distance

    
###Gluton algorithm#####
def trouve_plus_petit_chemin(chemin,tableau,index):
    mini_chemin=chemin.copy()
    distance_mini=float('inf')
    for i in range(0,len(chemin)):
        chemin.insert(i, tableau[index])
        if calculer_distance_total(chemin)<distance_mini:
            mini_chemin=chemin.copy()
            distance_mini=calculer_distance_total(chemin)
        chemin.remove(chemin[i])
    chemin=mini_chemin.copy()
    return chemin


def glouton(chemin, tableau):
    chemin.append(tableau[0])
    chemin.append(tableau[1])
    chemin.append(tableau[2])
    for i in range(3,len(tableau)):
        chemin = trouve_plus_petit_chemin(chemin, tableau,i).copy()
    return chemin

#Debut Algo
##Generation    
coordonnées_total=[]
for i in range(0, len(listVille)):
     coordonnées_total.append((listVille[i].latitude,listVille[i].longitude))

coordonnées_restreint=[]
for i in range(0,cities_number):
    coordonnées_restreint.append(coordonnées_total[i])

chemin=[]
population=[]

def initialize_20glutons_population(population,chemin,tableauDonnées):
    for i in range(0,20):
        chemin = glouton(chemin,tableauDonnées)
        population.append(chemin)
    return population

population=initialize_20glutons_population(population, chemin, coordonnées_restreint)
print(population)

# # Define parameters
# populationSize = 70
# mutationRate = 0.01
# maxGenerations = 70

# def createRandomIndividual(length):
#     return [random.randint(0,1) for _ in range(length)]

# def evaluateFitness(individual):
#     return sum(individual)

# def initializePopulation():
#     return [createRandomIndividual(10) for _ in range(populationSize)]

# def selectParent(population):
#     totalFitness = sum(evaluateFitness(individual) for individual in population)
#     r = random.uniform(0, totalFitness)
#     runningTotal = 0
#     for individual in population:
#         runningTotal += evaluateFitness(individual)
#         if runningTotal >= r:
#             return individual

# def crossover(parent1, parent2):
#     crossoverPoint = random.randint(1, len(parent1) - 1)
#     child1 = parent1[:crossoverPoint] + parent2[crossoverPoint:]
#     child2 = parent2[:crossoverPoint] + parent1[crossoverPoint:]
#     return child1, child2

# def mutate(individual):
#     for i in range(len(individual)):
#         if random.random() < mutationRate:
#             individual[i] = 1 - individual[i]

# def terminationConditionNotMet(generationCount):
#     return generationCount < maxGenerations

# def geneticAlgorithm():
#     population = initializePopulation()
#     generationCount = 0
    
#     while terminationConditionNotMet(generationCount):
#         newPopulation = []
        
#         while len(newPopulation) < len(population):
#             parent1 = selectParent(population)
#             parent2 = selectParent(population)
#             child1, child2 = crossover(parent1, parent2)
#             mutate(child1)
#             mutate(child2)
#             newPopulation.append(child1)
#             newPopulation.append(child2)
        
#         population = newPopulation
#         generationCount += 1
    
#     # Find and return the best individual in the final population
#     bestIndividual = max(population, key=evaluateFitness)
#     return bestIndividual

# # Example usage
# bestSolution = geneticAlgorithm()
# print("Best solution found:", bestSolution)

# ################FIN ALGO #############

