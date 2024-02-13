import  folium
import pandas as pd
import  csv
import  json

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
            ville = Ville(row[0], row[1])
            listVille.append(ville)



for i in range(0,len(listVille)):
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

print(nouveau_tableau)



# folium.PolyLine(nouveau_tableau, tooltip="Coast").add_to(m)


# folium.PolyLine(nouveau_tableau, tooltip="Coast").add_to(m)

m





m.save("map.html")