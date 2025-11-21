

import csv
"""
Exercice 4 :

Crée un fichier produits.csv

Ajoute 3 produits avec prix et quantité

Lis et affiche le contenu
"""
with open("produits.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Nom", "Prix", "Quantite"])
    writer.writerow(["PC", 1018, 100])
    writer.writerow(["Tablettes", 150, 20])
    writer.writerow(["Phone", 199, 88])


# Lecture CSV
with open("produits.csv", "r") as f:
    lecteur = csv.reader(f)
    for ligne in lecteur:
        print(ligne)