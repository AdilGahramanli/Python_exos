tableau = list(range(0, 10, 1))
print(tableau)

#IMPLEMENTER SWAP
def swap(tab, number1, number2):
    tab[number1], tab[number2] = tab[number2], tab[number1]

swap(tableau, 2, 8)
swap(tableau, 0, 5)
print(tableau)

n = len(tableau)
for temp in range(0,n):
    mini = temp
    for j in range(temp+1, n):
        if tableau[j] < tableau[mini]:
            mini = j
    if min is not temp:
        temp2=tableau[temp]
        tableau[temp]=tableau[mini]
        tableau[mini] = temp2

print(tableau)

