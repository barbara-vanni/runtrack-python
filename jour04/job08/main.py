# Écrire un programme qui calcule la somme de toutes les valeurs paires de la liste

L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]
print(L)

somme_paires = 0
for nombre in L:
    if nombre % 2 == 0:
        somme_paires += nombre
        print(nombre)


print("La somme des valeurs paires de la liste est :", somme_paires)



