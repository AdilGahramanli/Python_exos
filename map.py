import  folium
import pandas as pd
import  csv
import  json
import  math

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

cities_number=7

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
    

# print(datasMap)
# print(listVille[0].latitude, listVille[0].longitude)
nouveau_tableau=[]
for i in range(0, len(listVille)):
     nouveau_tableau.append((listVille[i].latitude,listVille[i].longitude))


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
    return round(d, 2)

# def gain():
def distances_villes_All(nouveau_tableau):
    for i in range(0, len(nouveau_tableau)):
        for j in range(i,len(nouveau_tableau)):
            print(distance_villes(nouveau_tableau,i,j))

def distances_villes_onlyOne(villes,k):
     for i in range(0, len(nouveau_tableau)):
          print(distance_villes(villes,i,k))

def distance_villes_simpleTrajet(chemin):
    distance=0
    for i in range(1, len(chemin)):
        distance = distance + distance_villes(chemin,i,i-1)
    return distance
    
        

def recupere_mini_combi(chemin, listeVilles, indexListeVilles):
    mini_combi=[]
    distance_mini=100000000
    for i in range(0, len(chemin)):
        chemin.insert(i, listeVilles[indexListeVilles])
        if distance_villes_simpleTrajet(chemin) < distance_mini:
            distance_mini = distance_villes_simpleTrajet(chemin)
            mini_combi = chemin.copy()
        chemin.remove(listeVilles[indexListeVilles])
    chemin = mini_combi.copy()

def glouton(nouveau_tableau, chemin):
    chemin.append(nouveau_tableau[0])
    chemin.append(nouveau_tableau[1])
    chemin.append(nouveau_tableau[2])

    for i in range(3, len(nouveau_tableau)):
         recupere_mini_combi(chemin, nouveau_tableau, i)

    return chemin

nouveau_tableau_petit=[]
for i in range(0,cities_number):
    nouveau_tableau_petit.append(nouveau_tableau[i])



print(nouveau_tableau_petit)
chemin=[]
glouton(nouveau_tableau_petit, chemin)
print(chemin)






# def gain():
# liste_trajets=[]
# liste_trajets.append(distances_villes_onlyOne(nouveau_tableau,0))
# print(nouveau_tableau[0][0], nouveau_tableau[0][1])
# folium.PolyLine(liste_trajets, tooltip="Coast").add_to(m)
# folium.PolyLine(nouveau_tableau, tooltip="Coast").add_to(m)
folium.PolyLine(nouveau_tableau_petit, tooltip="Coast").add_to(m)
m.save("map.html")