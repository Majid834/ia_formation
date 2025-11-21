"""
Les tuples (30 min)

Les tuples sont similaires aux listes, mais immuables (non modifiables).
"""
coordonnees = (10.5,20.7)

print("coordonnees => ", coordonnees )

# Cas d’usage : retour multiple d’une fonction

def stats(liste) :
    return (min(liste),max(liste),sum(liste)/len(liste)) 

resultat = stats([10,20,30])

print(" Min : ",resultat[0], "\n Max :", resultat[1], "\n Moyen", resultat[2])