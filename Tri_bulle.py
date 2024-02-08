tableau = list(range(0, 10, 1))
n = len(tableau)
print(tableau)

#IMPLEMENTER SWAP
def swap(tab, number1, number2):
    tab[number1], tab[number2] = tab[number2], tab[number1]

swap(tableau, 2, 8)
swap(tableau, 0, 5)
print(tableau)
permutation = True

while   permutation==True:
    permutation = False
    for i in range(0, len(tableau)-1):
        if i<9 and tableau[i+1] < tableau[i]:
            swap(tableau,i,i+1)
            permutation = True
    
            
print(tableau)
# if  i==len(tableau) and permutation==True:
#     i=0
#     permutation=False

#     for i in range(0,len(tableau)):
        
#         if tableau[i] > tableau[i+1]:
#             swap(tableau, i, i+1)
#             permutation==True
#             print(tableau)
            

# if i==len(tableau):
        #         if permutation==True:
        #             i=0
        #             permutation==False
        #             print(tableau)
# i=0
# temp=i+1
# permutations=list(range(1, 10,1))
# for i in range(len(permutations)):
#     permutations[i]=False

# print(permutations)







# # permutation = True
# # passage = 0

# # a=0
# # b=1


    
# def scope(tab, a, b):
#     if tab[a]<tab[b]:
#         a = a+1
#         b=b+1
        
#     else :
#         swap(tab, a, b)
#         a= a+1
#         b=b+1
        

# while   b!=10:
#     scope(tableau, a, b)
#     print(tableau)

# # while permutation == True:
# #     permutation = False
# #     passage = passage +1
# #     for en_cours in range(0, len(tableau) - passage):
# #         if tableau[en_cours] > tableau[en_cours + 1]:
# #             permutation = True
# #             swap(tableau, en_cours, en_cours+1)
        
# # print(tableau)

