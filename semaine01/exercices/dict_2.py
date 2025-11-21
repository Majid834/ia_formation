"""
Les dictionnaires (1h)

Les dictionnaires stockent des couples clé → valeur.
Ils sont essentiels pour la représentation des données en IA.
"""

etudiant = {
    "nom": "Majid",
    "age": 25,
    "note" : 16
}

print(etudiant)

for cle, val in etudiant.items():
    print(cle ," => ",val)

    """
    Exercice 3 :

Crée un dictionnaire produit = {"nom": "PC", "prix": 899.99, "stock": 15}

Diminue le stock de 3 après une vente

Affiche les infos mises à jour
    """

produit = {"nom": "PC", "prix": 899.99, "stock": 15}

produit["stock"] = produit["stock"] -3

for cle, val in produit.items():
    print(cle ," => ",val)