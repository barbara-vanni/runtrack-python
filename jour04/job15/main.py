# Écrivez un programme qui arrondi les nombres de la liste [22.4, 4.0, 16.22, 9.10, 11.00,
# 12.22, 14.20, 5.20, 17.50] Puis retourner la liste dans l’ordre croissant.
# SANS UTILISER DE FONCTION SYSTÈME (len, sort, round.....)



L = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

def my_len(string):
    count = 0

    for i in string:
        count += 1
    return count



def int_number(x: float) -> int:
    if x < int(x) + 0.5:
        return int(x)
    else:
        return int(x + 1)


def int_list(L: list) -> list:
    result = []
    for i in L:
        result = result + [int_number(i)]
    return result

def sort(L):
    n = my_len(L)
    for i in range(n):
        sort = True
        for j in range(0, n - i - 1):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
                sort = False
        if sort:
            break

result = int_list(L)
sort(result)

print("Liste arrondie et triée:", result)

