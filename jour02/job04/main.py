        
while True:

        N = int(input("Tapez la valeur de N : "))
        if N > 0:
            for i in range(1, N + 1):
                print("Table de multiplication de", i,":")
                for j in range(1, 11):
                    result = i * j
                    print(f"{i} x {j} = {result}")
            break
        else:
            print("La valeur de N doit être supérieure à 0. Veuillez réessayer.")