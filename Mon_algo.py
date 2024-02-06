tab_init = [3, 5, 7, 1, 0, 2, 8, 4]
tab_final = []
min = tab_init[0]
mini = 0

print(tab_init)
print(tab_final)

while len(tab_init) != 0:
    mini = 0
    min = tab_init[0]
    for i in range(len(tab_init)):
        if min > tab_init[i]:
            min = tab_init[i]
            mini = i
            
    tab_final.append(min)
    tab_init.pop(mini)
    print(tab_init)
    print(tab_final) 

print(tab_init)
print(tab_final)


# while len(tab_init) >= len(tab_final):
#     for i in range(len(tab_init)):
    
#         if tab_init[i] < min:
#             min = tab_init[i]
#             tab_final.append(min)
            
#             print(tab_final)


# while tab_init > tab_final:
#     for i in range(len(tab_init)):
#         if tab_init[i] < min:
#             min = tab_init[i]
#             index = i
#             print("hello")

#     tab_final.append(min)        
#     tab_init.pop(index)
    

# print(tab_init)
# print(tab_final)