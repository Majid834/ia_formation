#############################################################
"""
Scénario du TP

Tu dois analyser les ventes d’un magasin fictif pendant 12 mois.
Chaque mois a un chiffre d’affaires exprimé en euros.

Les ventes sont les suivantes (à recopier) :
Mois	Ventes (€)
Jan	12 500
Fév	15 200
Mar	17 800
Avr	13 600
Mai	19 300
Juin	22 400
Juil	20 500
Août	18 900
Sep	17 600
Oct	21 300
Nov	23 800
Déc	25 500
"""
"""
Travail demandé

Créer un tableau NumPy contenant toutes les ventes.

Afficher :

le chiffre d’affaires total de l’année

la moyenne mensuelle

le mois le plus faible

le mois le plus élevé

Reshaper le tableau en un tableau 3×4 (3 trimestres × 4 mois) et afficher la somme par trimestre.

Sauvegarder le tableau original en .npy et .csv.

Recharger les deux fichiers et vérifier que les données sont identiques.
"""
#####################################################################################
import numpy as np

def get_mois(a):
        mois = np.array([
        "Jan", "Fév", "Mar", "Avr", "Mai", "Juin",
        "Juil", "Août", "Sep", "Oct", "Nov", "Déc"
        ])
        if a>=0 or a<12:
            return mois[a]

# Créer un tableau NumPy contenant toutes les ventes.

t_vente = np.array([12500,15200,17800,13600,19300,22400,20500,18900,17600,21300,23800,25500])

print("le chiffre d’affaires total de l’année :" ,np.sum(t_vente) )

# la moyenne mensuelle
print("la moyenne mensuelle :" ,np.mean(t_vente))

# le mois le plus faible
print("le mois le plus faible : " ,np.min(t_vente) )

# le mois le plus élevé
m_max = np.max(t_vente);
index_m_max = np.argmax(t_vente)
print ("le mois le plus élevé :" ,m_max, get_mois(index_m_max))

# Reshaper le tableau en un tableau 3×4 (3 trimestres × 4 mois) et 

t_resh = np.reshape(t_vente, (3,4))

# afficher la somme par trimestre.
print ("somme trimestre 1 :" ,np.sum(t_resh[0]))
print ("somme trimestre 2 :" ,np.sum(t_resh[1]))
print ("somme trimestre 3" ,np.sum(t_resh[2]))

# sauv t_vente en npy et csv

np.save("tab_original.npy", t_vente)
np.savetxt("tab_original.csv", t_vente, delimiter=",")

# recharge les deux fichier
A = np.load("tab_original.npy")
B = np.loadtxt("tab_original.csv", delimiter=",")

#verfier si leux tableaux sont identique 

print("A == B? ", np.array_equal(A, B))