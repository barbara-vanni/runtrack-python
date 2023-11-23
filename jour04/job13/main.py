# Écrivez un programme qui supprime les doublons de la liste suivante :
# [10,20,30,20,10,50,60,40,80,50,40].
# SANS UTILISER DE FONCTION SYSTÈME (len, sort, round.....)

L = [10,20,30,20,10,50,60,40,80,50,40]
new_list = []

while L:
    min = L[0]  
    for i in L: 
        if i == min:
            L.remove(i)
    new_list.append(min)    

print(new_list)