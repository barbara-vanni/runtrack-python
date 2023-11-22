def reverse_string(word):
    index = len(word) - 1
    newList = []

    while index >= 0:
        newList.append(word[index])
        index = index - 1
    
    return newList

word = input("Entrez un mot : ")
reversed_list = reverse_string(word)
print(*reversed_list)
