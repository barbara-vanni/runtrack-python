chaine = "abcdefghijklmnopqrstuvwxyz" 

pyramide = ""
n = len(chaine)
# calcule de la longueur max en prenant la moitié de la longueur et +1 pour être sur que ce soit impair 
max_width = n // 2 + 1  

for i in range(1, n + 1):
    pyramide += chaine[i - 1]
    # si l'indice i est impair, puisqu'on à besoin de sauter deux caractère à chaque ligne 
    if i % 2 == 1:
        print(pyramide)