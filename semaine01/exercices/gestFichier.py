# ecrirture

with open("data.txt", "w") as f:
    f.write("Bonjour tout le monde IA\nPython est génial!")



#lecture

with open("data.txt", "r") as f:
    continu = f.read()

print(continu)