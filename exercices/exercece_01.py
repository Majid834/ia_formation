"""
Fonctions utiles :

len(liste) → longueur

sum(liste) → somme

max(liste) / min(liste) → valeurs extrêmes

sorted(liste) → tri

Exercice 1 :

Crée une liste notes = [12, 17, 9, 14, 18]

Calcule la moyenne

Trie la liste par ordre croissant
"""

# liste note :
notes = [12, 17, 9, 14,18]

moyen = sum(notes) / len(notes)
print("Moyen des notes => ", moyen,"/ 20")

print("Liste des notes =>", notes)

print("Liste des notes trié=>", sorted(notes))
