"""
Les listes (45 min)

Les listes sont très utilisées en IA pour stocker des collections de données (valeurs, vecteurs, échantillons, etc.)
"""

nombres = [10, 20, 30, 40]

nombres.append(50)

print("liste Nombres => ", nombres)

#suppression 

nombres.remove(20)

print("liste Nombres => ", nombres)
print("lent", len(nombres) )

print("sorted-tri =>", sorted(nombres))
print("max =>", max(nombres))
print("min => ", min(nombres))
print("sum =>",sum(nombres))