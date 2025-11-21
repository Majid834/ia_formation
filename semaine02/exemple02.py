import pandas as pd


s = pd.Series([10, 20, 30, 40, 50])
#print(s)

#print(s[2])  # Accès à l'élément à l'index 2

df = pd.DataFrame({
    "Nom": ["Alice", "Bob", "Charlie"],
    "Âge": [25, 30, 35],
    "Ville": ["Paris", "Lyon", "Marseille"]
})
print(df)
