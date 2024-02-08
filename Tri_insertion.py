T=list(range(10))

n=len(T)
#Fonction swap
def swap(tab, number1, number2):
    tab[number1], tab[number2] = tab[number2], tab[number1]

swap(T, 0, 5)
swap(T, 2, 8)
print(T)

for i in range(1, len(T)):
    temp = T[i]
    j = i
    while   j>0 and T[j-1]>temp:
            swap(T,j,j-1)
            j=j-1
    T[j] = temp

print(T)
