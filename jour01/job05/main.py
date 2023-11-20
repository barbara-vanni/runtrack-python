print("--------------JOB05 DE BASE--------------")

alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']

alpha.reverse()

print (*alpha)


# EXO + : sans utiliser reverse 

print("--------------SANS UTILISER REVERSE--------------")

alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']

index = len(alpha) - 1
newList = []

while index >= 0:
    newList.append(alpha[index])
    index = index - 1

print(*newList)



# EXO ++ : mélanger mon alphabet puis le retrier 
#bubble sort 
#fonction.random
# commment 

print("--------------RANDOMISER + RANGER--------------")

import random

alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']
random.shuffle(alpha)
print(*alpha)

