# Écrire un programme qui trie dans l’ordre croissant une liste passée en paramètre.
# SANS UTILISER DE FONCTION SYSTÈME (len, sort, round.....)

L = [-15, 43, 15, 1, 23, -62, 76]
new_list = []

while L:
    min = L[0]  
    for i in L: 
        if i < min:
            min = i
    new_list.append(min)
    L.remove(min)    

print(new_list)
