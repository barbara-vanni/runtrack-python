print("--------------JOB05 DE BASE--------------")

alpha = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "x",
    "y",
    "z",
]

alpha.reverse()

print(*alpha)


# EXO + : sans utiliser reverse

print("--------------SANS UTILISER REVERSE--------------")

alpha = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "x",
    "y",
    "z",
]

index = len(alpha) - 1
newList = []

while index >= 0:
    newList.append(alpha[index])
    index = index - 1

print(*newList)


# EXO ++ : mélanger mon alphabet puis le retrier

print("--------------RANDOMISER + RANGER--------------")

import random

alpha = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "x",
    "y",
    "z",
]
random.shuffle(alpha)
print("Alphabet mélangé:", *alpha)

codes_ascii = [ord(letter) for letter in alpha]
print("En ASCII:", codes_ascii)


def bubble_sort(codes_ascii):
    n = len(codes_ascii)
    for i in range(n):
        sort = True
        for j in range(0, n - i - 1):
            if codes_ascii[j] > codes_ascii[j + 1]:
                codes_ascii[j], codes_ascii[j + 1] = codes_ascii[j + 1], codes_ascii[j]
                sort = False
        if sort:
            break


bubble_sort(codes_ascii)


alpha_sort = "".join([chr(code) for code in codes_ascii])
# join est utilisée pour concaténer tous les caractères de la liste en une seule chaîne de caractères. 
# '' comme séparateur vide 
print("Alphabet trié:", alpha_sort)

# codes_ascii.sort()

# print(codes_ascii)

# alpha= [chr(code) for code in codes_ascii]

# print(*alpha)
