
import csv

with open("notes.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Nom", "Note"])
    writer.writerow(["Majid", "18"])
    writer.writerow(["Asma", "15"])


#Lecure

with open("notes.csv", "r") as f :
    lecteur = csv.reader(f)

    for row in lecteur:
        print(row)