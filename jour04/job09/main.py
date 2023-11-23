# Écrire un programme qui récupère la valeur, maximum et le minimum des éléments de
# la liste.

L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
print(L)

def max_min(liste):
    maxi = liste[0]
    min = liste[1]
    
    for i in liste:
        if i >= maxi:
            maxi = i
        for j in liste:
            if j <= min:
                min = j
    return maxi,min

print(max_min(L))

