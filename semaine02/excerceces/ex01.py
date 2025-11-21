# creer un DataFrame de 4 personnes contenant les colonnes suivantes: "Nom", "Âge", "Ville", "Salaire"
import pandas as pd

data = {"Nom": ["Alice", "Bob", "Charlie", "Diana"],
        "Age": [25, 30, 35, 28],
        "Ville": ["Paris", "Lyon", "Marseille", "Nice"],
        "Salaire": [50000, 60000, 70000, 55000]}
df = pd.DataFrame(data)
# Afficher le DataFrame
print(df)

# affiche la colonne "Salaire"
print(df["Salaire"])

#ajouter une nouvelle colonne "Année d'embauche" avec des valeurs correspondantes
df["Année d'embauche"] = [2018, 2016, 2015, 2019]
print(df)

