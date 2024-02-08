def swap(A, i, j):
   A[i], A[j] = A[j], A[i]

# def insertionSort(inputArr):
#     print("implement me")

# def selectionSort(inputArr):
#     print("implement me")

def bubbleSort(list):
    permutation = True
    while   permutation==True:
        permutation = False
        for i in range(0, len(list)-1):
            if i<9 and list[i+1] < list[i]:
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

# insertion_list = insertionSort(list.copy())

# selection_list = selectionSort(list.copy())

bubble_list = bubbleSort(swapped_list)

# shell_list = shellSort(list.copy())

# heap_list = heapSort(list.copy())

# Affichage des résultats
# print("Liste non triée")
# print(list)
# print("Swap des deux premiers éléments")

# print(swapped_list)

# print("Insertion")
# print(insertion_list)

# print("Selection")
# print(selection_list)

print("Bubble")
print(bubble_list)

# print("Shell")
# print(shell_list)

# print("Heap")
# print(heap_list)