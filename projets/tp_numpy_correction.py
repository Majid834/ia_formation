import numpy as np

def get_mois(a):
    mois = np.array([
        "Jan", "Fév", "Mar", "Avr", "Mai", "Juin",
        "Juil", "Août", "Sep", "Oct", "Nov", "Déc"
    ])
    if 0 <= a < 12:
        return mois[a]
    return "Index invalide"


# 1. Tableau des ventes
t_vente = np.array([12500, 15200, 17800, 13600, 19300, 22400,
                    20500, 18900, 17600, 21300, 23800, 25500])

print("Chiffre d’affaires total :", np.sum(t_vente))
print("Moyenne mensuelle :", np.mean(t_vente))

# 2. Mois le plus faible et le plus élevé
index_min = np.argmin(t_vente)
index_max = np.argmax(t_vente)

print("Mois le plus faible :", np.min(t_vente), get_mois(index_min))
print("Mois le plus élevé :", np.max(t_vente), get_mois(index_max))

# 3. Reshape + somme trimestrielle
t_resh = t_vente.reshape(3, 4)
for i, trimestre in enumerate(t_resh, start=1):
    print(f"Somme du trimestre {i} :", trimestre.sum())

# 4. Sauvegarde
np.save("tab_original.npy", t_vente)
np.savetxt("tab_original.csv", t_vente, fmt="%d", delimiter=",")

# 5. Rechargement et vérification
A = np.load("tab_original.npy")
B = np.loadtxt("tab_original.csv", delimiter=",")

print("A == B ?", np.array_equal(A, B))
