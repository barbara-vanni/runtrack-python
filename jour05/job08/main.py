# voici ma liste à trier 
List = [45,78,92,32,67,89,14,53,76,41,60,85,23,94,50]

# on crée un fonction qui prenne ma list en paramètre 
def my_sort(List):
    # on a besoin de la longueur de notre liste pour connaitre le nombre d'index à "trier"
    # et d'initialiser un compteur pour connaître le nombre de fois que l'on va itérer dessus
    n = len(List)
    count = 0
    # on commence par une boucle qui va tourner autant de fois qu'il y a de nombre dans notre liste 
    for i in range(n):
        # une boucle dans une boucle pour que itérer sur chaque index de la liste
        for j in range(0, n - i - 1):
            # on regarde si l'index J est supérieur à celui à sa droite (J+1)
            if List[j] > List[j + 1]:
                # si c'est le cas on inverse index (J) et (J+1)
                List[j], List[j + 1] = List[j + 1], List[j]
                # et on ajoute 1 à notre compteur
                count += 1
                # on le print
    print ("Le nombre total de coup nécessaire:", count)
    return (List)

# on place le "return" de notre fonction dans une variable sinon on peut pas la print 
list_sort = my_sort(List)
# et on affiche dans notre terminal 
print("Liste triée:", list_sort)