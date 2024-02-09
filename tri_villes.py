from tkinter import *
from tkinter import filedialog
import csv
import  math
import  geopy


class Ville :
    def __init__(self, nom_commune, codes_postaux, latitude, longitude, dist, distanceFromGrenoble):
        self.nom_commune = nom_commune
        self.codes_postaux = codes_postaux
        self.latitude = latitude
        self.longitude = longitude
        self.dist = dist
        self.distanceFromGrenoble = distanceFromGrenoble


def loadFile():
    listVille.clear()
    filename = filedialog.askopenfilename(initialdir="./",
                                          title="Selection du Fichier",
                                          filetypes=(("Text files",
                                                      "*.csv*"),
                                                     ("all files",
                                                      "*.*")))
    changeLabelFile("Fichier : "+filename)
    with open(filename, 'r', encoding='UTF-8') as file:
        csvreader = csv.reader(file)
        next(csvreader)  # skip header line
        for row in csvreader:
            data = row[0].split(";")
            try:
                ville = Ville(data[8], data[9], float(data[11]), float(data[12]), float(data[13]), 0)
                ville.distanceFromGrenoble = getDistanceFromGrenoble(ville)
                listVille.append(ville)
            except:
                continue


def getDistanceFromGrenoble(ville):

    # r=6371**3

    # lat_Grenoble = 45.18675902087716 
    # long_Grenoble = 5.7362964134908285

    # phi1= lat_Grenoble * math.pi/180
    # phi2 = ville.latitude*math.pi/180
    # deltaPhi = (ville.latitude - lat_Grenoble) * math.pi/180
    # deltaZegma = (ville.longitude - long_Grenoble) * math.pi/180

    # a=math.sin(deltaPhi/2)*math.sin(deltaPhi/2)+math.cos(phi1)*math.cos(phi2)*math.sin(deltaZegma/2)*math.sin(deltaZegma/2)
    # c=2*math.atan2(math.sqrt(a), math.sqrt(1-a))
    # d=r*c
    return geopy.distance.geodesic((ville.latitude, ville.longitude), (45.166672, 5.71667)).m



def isLess(listVille, i, j):
    distanceVille1 = getDistanceFromGrenoble(listVille[i])
    distanceVille2 = getDistanceFromGrenoble(listVille[j])
    if distanceVille1 < distanceVille2:
        return True


def swap(listVille, i, j):
    if isLess(listVille, i, j)!=True:
        listVille[i], listVille[j] = listVille[j], listVille[i]
    return listVille



def changeLabelFile(text):
    labelFileExplorer = Label(fenetre,
                              text=text,
                              width=120, height=4,
                              fg="black", background="#579BB1")
    labelFileExplorer.place(x=150, y=offset + 40)


def changeLabelButtonSubmit(text):
    buttonValidation['text'] = text
    buttonValidation.place(x=150, y=offset + 120)


def onSelectTypeTri(event):
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        data = event.widget.get(index)
        global typeTriSelection
        typeTriSelection = data
        changeLabelButtonSubmit("Lancement du {}".format(data))


def sort():
    # effacement de la liste affichée
    listVilleSortedBox.delete(0, END)
    listVilleSorted = listVille.copy()

    if typeTriSelection == "Tri par insertion":
        listVilleSorted = insertsort(listVilleSorted)
    elif typeTriSelection == "Tri par sélection":
        listVilleSorted = selectionsort(listVilleSorted)
    elif typeTriSelection == "Tri à bulles":
        listVilleSorted = bubblesort(listVilleSorted)
    elif typeTriSelection == "Tri de Shell":
        listVilleSorted = shellsort(listVilleSorted)
    elif typeTriSelection == "Tri par fusion":
        listVilleSorted = mergesort(listVilleSorted)
    elif typeTriSelection == "Tri par tas":
        listVilleSorted = heapsort(listVilleSorted)
    elif typeTriSelection == "Tri rapide":
        listVilleSorted = quicksort(listVilleSorted)

    for ville in range(len(listVilleSorted)):
        listVilleSortedBox.insert(END, listVilleSorted[ville].nom_commune + " - " + str(listVilleSorted[ville].distanceFromGrenoble))
        listVilleSortedBox.itemconfig(ville, fg="black")

    listVilleSortedBox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listVilleSortedBox.yview)


def insertsort(listVille):
    # j=0
    # for i in range(1, len(listVille)): # boucle qui avance
    #     j=i
    #     while j>0 and isLess(listVille,j-1,j)!=True:
    #         swap(listVille, j, j-1)
    #         j=j-1 # fait reculer le j
    return listVille


def selectionsort(listVille):
    
    nb = len(listVille)
    for temp in range(0, nb):                   #temp sélectionnera chaque valeur du tableau
        mini=temp                               #initialement, temp est considérée comme mini
        for j in range(temp+1,nb):              #j va chercher toutes les valeurs à droite de temp
            if listVille[j] < listVille[mini]:    #j compare sa valeur avec mini
                mini = j                        #si j trouve une valeur moindre alors mini prend la même valeur que j
        if mini != temp:
            swap(listVille, temp, mini)          #fin de la boucle, on a trouvé la valeur minimale
                                                #et on va la placer à l'endroit du temp
                                         
    return listVille


def bubblesort(listVille):
    # permutation = True
    # while   permutation==True:
    #     permutation = False
    #     for i in range(0, len(list)-1):
    #         if list[i+1] < list[i]:
    #             swap(list,i,i+1)
    #             permutation = True
    return listVille


def shellsort(listVille):
    print("implement me !")
    return listVille


def mergesort(listVille):
    print("implement me !")
    return listVille


def heapsort(listVille):
    print("implement me !")
    return listVille


def quicksort(listVille):
    print("implement me !")
    return listVille


# Creation de la fenêtre
fenetre = Tk()
width = 1000
height = 180
offset = 10
listVille = []
listTri = ["Tri par insertion",
           "Tri par sélection",
           "Tri à bulles",
           "Tri de Shell",
           "Tri par fusion",
           "Tri par tas",
           "Tri rapide"]

typeTriSelection = "Tri par insertion"

labelFileExplorer = Label()
canvas = Canvas(fenetre, width=width + 2*offset,
                height=height + 2*offset, bg='white')
buttonValidation = Button(command=sort)

list = Listbox(fenetre, width=20, height=len(listTri), selectmode="single")
list.place(x=offset, y=offset)
list.bind("<<ListboxSelect>>", onSelectTypeTri)

for typeTri in range(len(listTri)):
    list.insert(END, listTri[typeTri])
    list.itemconfig(typeTri, fg="black")

buttonFile = Button(
    fenetre, text="Importation du fichier", command=loadFile)
buttonFile.place(x=150, y=offset)

changeLabelButtonSubmit("Lancement du {}".format(typeTriSelection))

changeLabelFile("Aucun Fichier ...")

canvas.pack()

listVilleSortedBox = Listbox(
    fenetre, width=100, height=25, selectmode="single")
listVilleSortedBox.pack(side=LEFT, fill=BOTH)

scrollbar = Scrollbar(fenetre, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=BOTH)
fenetre.mainloop()
