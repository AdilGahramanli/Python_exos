def swap(A, i, j):
   A[i], A[j] = A[j], A[i]



def isLess(listVille, i, j):
    # distanceVille1 = getDistanceFromGrenoble(listVille[i])
    # distanceVille2 = getDistanceFromGrenoble(listVille[j])
    
    if listVille[i] <= listVille[j]:
        return True

def insertionSort(inputArr):
    for i in range(1, len(inputArr)): 
        j=i
        while j>0 and inputArr[j-1]>inputArr[j]:
            swap(inputArr, j, j-1)
            j=j-1 
        
    return inputArr

def selectionSort(inputArr):
    nb = len(inputArr)
    for temp in range(0, nb):                   #temp sélectionnera chaque valeur du tableau
        mini=temp                               #initialement, temp est considérée comme mini
        for j in range(temp+1,nb):              #j va chercher toutes les valeurs à droite de temp
            if inputArr[j] < inputArr[mini]:    #j compare sa valeur avec mini
                mini = j                        #si j trouve une valeur moindre alors mini prend la même valeur que j
        if mini != temp:
            swap(inputArr, temp, mini)          #fin de la boucle, on a trouvé la valeur minimale
                                                #et on va la placer à l'endroit du temp
                                                #on replace mini sur temps pour pouvoir chercher le nouveau mini
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

# def quickSort(inputArr):
#     pivot = inputArr[len(inputArr)-1]
#     max = inputArr[0]
#     min = 0
#     permutation == 
#     for i in range(0, len(inputArr)):
#         if isLess(inputArr, i, pivot) != True:
#             max = inputArr[i]
#             for j in range(i, len(inputArr)):
#                 if isLess(inputArr, j, pivot)==True:
#                     min=inputArr[j]
#                     permutation == False

#     return pivot


#     print("quicksort implementation")

# def quickSort(inputArr, premier, dernier):
#     dernier = len(inputArr)-1
#     premier = inputArr[0]
    

#     if len(inputArr)>2:
#         for i in range(premier, dernier):                           #on parcourt du premier au dernier
#             while i != dernier:                                     #Tant que i n'a pas atteint le dernier
#                 if isLess(inputArr, i, dernier)==False:             # si je trouve une valeur plus grande que le dernier...
#                     for j in range(i+1, dernier):                   #... je parcourt à partir de là avec j...
#                         if isLess(inputArr, j, dernier)== True:     #... si j a une valeur plus petite que le dernier...
#                             swap(inputArr, i, j)                    #... intervertir la valeur grande et la valeur petite (petite s'éloigne du dernier et grande s'en rapproche)
#                         if i == dernier-1:                          #MAIS si j'arrive au dernier sans trouver de plus petit alors...
#                             swap(inputArr, premier, dernier)        #... on intervertit dernier et input[i]
#                             premier =+1                             # Proédure trop compliquée - STOP !
#             dernier =-1


def partitionner(inputArr, premier, dernier, pi):
    swap(inputArr, pi, dernier)
    # pi = dernier
    j = premier
    

    for i in range(premier, dernier):
        if inputArr[i]<=inputArr[pi]:
            swap(inputArr, i, j)
            j= j+1
    swap(inputArr, dernier, j)
    return j


def quickSort(inputArr, premier, dernier):
    pi = dernier
    if premier < dernier:
        pi = partitionner(inputArr, premier, dernier, pi)
        quickSort(inputArr, premier, pi-1)
        quickSort(inputArr, pi+1, dernier)
    return inputArr






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

quick_list = quickSort(list.copy(), 0, len(list)-1)

# Affichage des résultats
# print("Liste non triée")
# print(list)
# print("Swap des deux premiers éléments")

# print(swapped_list)
print ("list non sorted")
print (list.copy())

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

print("Quick")
print(quick_list)