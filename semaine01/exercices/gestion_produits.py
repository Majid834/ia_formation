produits = {"Clavier": 49.99, "Souris": 19.99, "Écran": 149.99}

# Ajouter un produit
produits["Casque"] = 29.99

produits["Webcam"] = 39.99

# Afficher tous les produits
for nom, prix in produits.items():
    print(f"{nom} : {prix} €")
