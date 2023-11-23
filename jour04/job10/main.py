# Écrire un programme qui calcule le produit de toutes les valeurs de la liste comprises
# dans l’intervalle [25, 90]

L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
print(L)

produit = 1
for nombre in L:
    if nombre >= 25 and nombre <= 90 :
        produit *= nombre
        print(nombre)


print("Le produit des valeurs comprise entre 25 et 90 de la liste est :", produit)