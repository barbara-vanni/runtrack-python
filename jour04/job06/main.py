list=[12, 22, 32, 52, 62, 72, 82]
print("Ancienne liste:", list)

def change_last_first(L):
    if not L:
        print("La liste est vide")
        return

    first = L[0]
    L[0] = L[-1]
    L[-1] = first

    return L

new_list = change_last_first(list)

print("Nouvelle liste:", new_list)