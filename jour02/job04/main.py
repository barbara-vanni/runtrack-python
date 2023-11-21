

while True:
    n = int(input("Tapez la valeur de n : "))
    
    if n > 0:
        print("La table de multiplication de", n, "est :")
        for i in range(1, 11): 
            print(i, "x", n, "=", i * n)
        break
    else:
        print("La valeur de n doit être supérieure à 0. Veuillez réessayer.")