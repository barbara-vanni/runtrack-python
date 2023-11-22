a = int(input("Tapez la valeur de a : "))
b = int(input("Tapez la valeur de b : "))       
c = int(input("Tapez la valeur de c : "))



if a <= 0 or b <= 0 or c <= 0 :
    print ("les valeurs doivent être supérieur à 0 !")

if a == b == c :
    print ("votre triangle est un triangle équilatéral")   

elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    print ("votre triangle est un triangle rectangle")
        
elif a == b != c or a == c !=b or c == b != a:
    print("Il s'agit d'un triangle isocèle")
    
elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2 and a == b != c or a == c != b or c == b != a:
    print("Votre triangle est un triangle rectangle et isocèle")
    

    


