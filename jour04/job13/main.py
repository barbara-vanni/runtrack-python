# Écrivez un programme qui supprime les doublons de la liste suivante :
# [10,20,30,20,10,50,60,40,80,50,40].
# SANS UTILISER DE FONCTION SYSTÈME (len, sort, round.....)

L = [10,20,30,20,10,50,60,40,80,50,40]
new_list = []

def my_len(string):
    count = 0

    for i in string:
        count += 1
    return count

for j in L:
    if j not in new_list:
        new_list += [j]
    

# min = L[0]  
for i in range (my_len(new_list)): 
    for k in range (0, my_len(new_list) -i -1):
        if new_list[k] > new_list[k + 1]:
            new_list[k], new_list[k + 1] = new_list[k + 1], new_list[k]

print(new_list)