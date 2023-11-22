a = float(input("Taille de a: "))
b = float(input("Taille de b: "))
c = float(input("Taille de c: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Merci de mettre des valeurs supérieur ou égal à 0")
    a = float(input("Taille de a: "))
    b = float(input("Taille de b: "))
    c = float(input("Taille de c: "))

if a + b > c and a + c > b and b + c > a:
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2 and a == b != c or a == c != b or c == b != a:
        print("C'est un triangle rectangle et isocèle")
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("C'est un triangle rectangle")
    elif a == b != c or a == c !=b or c == b != a:
        print("C'est un triangle isocèle")
    elif a == b and a == c:
        print("C'est un triangle equilatéral")
    else:
        print("C'est un triangle quelconque")
else:
    print("Les valeurs données ne permettent pas de former un triangle")
