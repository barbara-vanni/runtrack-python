montant_initial = 1500
taux_rendement_annuel = (10/100)

gain_annuel = (taux_rendement_annuel * montant_initial)

print( "Gain annuel initial:", gain_annuel)

montant_initial += gain_annuel

print( "Montant annuel total:", montant_initial)

montant_initial += 5000
taux_rendement_annuel += (2/100)


nouveau_gain_annuel = (taux_rendement_annuel * montant_initial)
print("Nouveau gain annuel après augmentation du capital et du taux de rendement :", nouveau_gain_annuel)

montant_initial += nouveau_gain_annuel

print( "Montant annuel total:", montant_initial)


retrait = ((10/100) * nouveau_gain_annuel)
# print(retrait)
nouveau_gain_annuel -= retrait
# print(nouveau_gain_annuel)
taux_rendement_annuel -= (1/100)


# print(taux_rendement_annuel)


nouveau_gain_final = nouveau_gain_annuel + (taux_rendement_annuel * nouveau_gain_annuel)
montant_initial += nouveau_gain_final
print("Nouveau gain après retrait et diminution du rendement :", nouveau_gain_final)
print("Montant final:", montant_initial)



