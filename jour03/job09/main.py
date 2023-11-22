def moyenne(note1, note2, note3):
    calcul = round((note1 + note2 + note3) / 3)
    return (calcul)

note1 = float(input("Note 1 : "))
note2 = float(input("Note 2 : "))
note3 = float(input("Note 3 : "))

moyenne_etudiant = moyenne(note1, note2, note3)
print(moyenne_etudiant)

if moyenne_etudiant >= 15 and moyenne_etudiant <= 20:
    print("Très bon élève")
elif moyenne_etudiant >= 11 and moyenne_etudiant <= 14:
    print("Bon élève")
elif moyenne_etudiant >= 8 and moyenne_etudiant <= 10:
    print("Élève moyen")
elif moyenne_etudiant >= 0 and moyenne_etudiant <= 7:
    print("Élève devant faire des efforts")
elif moyenne_etudiant == 42:
    print("Mon appartement sent bon l'acajou")
else:
    print("Moyenne invalide")
