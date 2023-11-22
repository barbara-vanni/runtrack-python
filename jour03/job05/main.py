def calcule(num1, operator, num2):
    
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    
    elif operator == '/':
        if num2 != 0: 
            return num1 / num2
        else:
            return "Erreur : Division par zéro"
    elif operator == '%':
        if num2 != 0:  
            return num1 % num2
        else:
            return "Erreur : Modulo par zéro"
    else :
        return "L'opérateur n'est pas reconnu (+, -, *, /, %)"
        
    
resultat= calcule(5, '+', 3)
print (resultat)

resultat= calcule(4, '*', 6)
print (resultat)

resultat= calcule(55, '/', 3)
print (resultat)

resultat= calcule(9, '-', 3)
print (resultat)

    