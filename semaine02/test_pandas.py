import pandas as pd

data = {"Nome": ["Ana", "Bruno", "Carla"],
         "Age": [23, 35, 29],
         "City": ["Lisbon", "Porto", "Coimbra"]}
df = pd.DataFrame(data)
# appel differents methodes
#print(df.head())  # Affiche les premières lignes du DataFrame
#print(df.describe())  # Affiche des statistiques descriptives
print(df["City"])  # Affiche la colonne "City"
print(df.sort_values("Age"))
#print(df)
# Output:   
