# Écrire un programme qui trie dans l’ordre croissant une liste passée en paramètre.
# SANS UTILISER DE FONCTION SYSTÈME (len, sort, round.....)

L = [-15, 43, 15, 1, 23, -62, 76]
new_list = []

def my_len(string):
    count = 0

    for i in string:
        count += 1
    return count


while L:
    min_index = 0
    for i in range(1, my_len(L)):
        if L[i] < L[min_index]:
            min_index = i

    new_list += [L.pop(min_index)]

print(new_list)


