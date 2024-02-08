def swap(A, i, j):
   A[i], A[j] = A[j], A[i]



def insertionSort(inputArr):
    for i in range(1, len(inputArr)): # boucle qui avance
        j=i
        while j>0 and inputArr[j-1]>inputArr[j]:
            swap(inputArr, j, j-1)
            j=j-1 # fait reculer le j
        
    return inputArr

def selectionSort(inputArr):
    nb = len(inputArr)
    for temp in range(0, nb):                   #temp sélectionnera chaque valeur du tableau
        mini=temp                               #initialement, temp est considérée comme mini
        for j in range(temp+1,nb):              #j va chercher toutes les valeurs à droite de temp
            if inputArr[j] < inputArr[mini]:    #j compare sa valeur avec mini
                mini = j                        #si j trouve une valeur moindre alors mini prend la même valeur que j
        if mini != temp:                        #fin de la boucle, on a trouvé la valeur minimale
            inputArr[temp] = inputArr[mini]     #et on va la placer à l'endroit du temp
            inputArr[mini] = temp               #on replace mini sur temps pour pouvoir chercher le nouveau mini
    return inputArr

def bubbleSort(list):
    permutation = True
    while   permutation==True:
        permutation = False
        for i in range(0, len(list)-1):
            if list[i+1] < list[i]:
                swap(list,i,i+1)
                permutation = True
    return list

def shellSort(inputArr):
    print("implement me")

def heapSort(inputArr, indexStart, indexEnd):
    print("implement me")

# Création de list
import random

list_size = 8
list = [random.randint(0, list_size * 2) for _ in range(list_size)]

# Calculs, performances
swapped_list = list.copy()
swap(swapped_list, 0, 1)


insertion_list = insertionSort(list.copy())

selection_list = selectionSort(list.copy())

bubble_list = bubbleSort(list.copy())

shell_list = shellSort(list.copy())

# heap_list = heapSort(list.copy())

# Affichage des résultats
# print("Liste non triée")
# print(list)
# print("Swap des deux premiers éléments")

# print(swapped_list)

print("Insertion")
print(insertion_list)

print("Selection")
print(selection_list)

print("Bubble")
print(bubble_list)

print("Shell")
print(shell_list)

print("Heap")
# print(heap_list)