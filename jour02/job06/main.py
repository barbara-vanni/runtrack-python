for num in range(2,1001):
    prime = True
    for i in range(2,num):
        if (num%i == 0):
            prime = False
    if prime:
       print (num)

# ---version more pythonic askip---- 

for num in range(2,1001):
    if all(num%i!=0 for i in range(2,num)):
       print (num)