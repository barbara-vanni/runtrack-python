# Écrire un programme qui créer la liste d’entiers L = [7, 11, 42, 39, 2], votre programme
# devra pouvoir modifier la liste en augmentant de 1 la valeur de chaque élément de la
# liste

L = [7, 11, 42, 39, 2]
print(L)

for i in range(len(L)):
    L[i] += 1

print (L)

