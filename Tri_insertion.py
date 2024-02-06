T=list(range(10))
T[0]=5
T[5]=0
T[8] = 2
T[2] = 8
n=len(T)
print(T)
temp=0
j=0

for i in T[1:n]:
    print(i)
    temp = T[i]
    j=i

    while j>0 & T[j-1]>temp:
        swap(T[j], T[j-1])
        j = j-1

    T[j] = temp

print(T)