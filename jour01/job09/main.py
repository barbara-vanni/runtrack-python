nom = "pull bleu"
prix_unitaire = 50
quantite = 100

print("Produit:", nom)
print("Prix unitaire:", prix_unitaire)
print("Quantité en stock:", quantite)
print("\n")

quantite_achetee = int(input("Combien de pull bleu voulez-vous : "))
quantite += quantite_achetee


prix_unitaire *= 1.10


print("Produit:", nom)
print("Nouveau prix unitaire après inflation:", prix_unitaire)
print("Nouvelle quantité en stock:", quantite)

