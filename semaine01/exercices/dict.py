my_dict = (
    {"nom": "pouchette","prix": "15"},
     {"nom": "pc","prix": "255"},
      {"nom": "phone","prix": "190"},
)

for i in range(len(my_dict)):
    print("produi", i+1, my_dict[i])


index = 0
print("nom : ", my_dict[1]["nom"])
print("Prix de produit ", index+1,"(", my_dict[index]["nom"],")","est : ", my_dict[1]["prix"], "€")

