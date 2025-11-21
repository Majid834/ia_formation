"""
Les sets sont des ensembles sans doublons. Très utiles pour filtrer ou vérifier l’unicité.
"""

valeurs ={1,2,2,3}

print(valeurs)

# exercice
#Crée une liste données = [1, 2, 2, 3, 4, 4, 5]
donnees = [1, 2, 2, 3, 4, 4, 5]
my_set =set()
print("my_set 0 => " ,my_set)
for i in donnees:
    #print(donnees[i])
    my_set.add(i)

print("liste donnees => " ,donnees)
print("my_set 1 => " ,my_set)
