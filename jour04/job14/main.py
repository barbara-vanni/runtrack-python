# Créer un programme contenant une fonction nommée “my_long_word”. Cette fonction
# doit prendre deux paramètres, un chiffre entier et une chaîne de caractère.
# Cette fonction doit retourner les mots plus long que le chiffre passé en paramètre.


def my_long_word(n, phrase):
    long_word = ""
    actual_word = ""
    compteur = 0
    
    for caractere in phrase:
        if caractere != ' ' and caractere != ",":
            actual_word += caractere
            compteur += 1
        elif actual_word:
            if compteur > n:
                long_word += actual_word + " "

            actual_word = ""
            compteur = 0
    
    if actual_word and compteur > n:
        long_word += actual_word + " "

    if long_word:
        long_word = long_word[:-1]
    
    return long_word

resultat = my_long_word(4, "Do not repeat yourself")
print(resultat)

