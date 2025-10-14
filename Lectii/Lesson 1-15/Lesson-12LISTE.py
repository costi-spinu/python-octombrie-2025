# customers = ['Bob','Anna','Joe','Bob','Nick']
# if ('Bob' in customers):
#     print("Bob is our customer")
# else:
#     print("Sorry")


# list1 = [1,2,3,4,5]
# list2 = list1
# list3 = [6,7,8]
# print(list2 is list1) #True
# print(list3 is list1) #False


# categorie = ["Drama", "Comedy", "Mystery","Romance"]
# for film in categorie:
#     print(film)


# categorie = ["Drama", "Comedy", "Mystery", "Romance"]
# for i in range(len(categorie)):
#     print(categorie[i])


# LISTE ADAUGA ALEMENTE - METODE 2.7
category = ["Drama", "Comedy", "Mystery", "Romance"]
for i in range(len(category)):
    if i == 2:
        print(
            "ai o reducere la produsul:" + category[i]
        )  # adaugare la un produs din lista o referinta

category.append("Produs nou")  # adaugam un singur element la sfarsitul listei
print(category)
category2 = ["casa", "masa"]
category.extend(
    category2
)  # adaugam o lista de elemente (mai multe elemente din alta lista)
print(category)
category.insert(1, "Produs adaugat ")  # adaugat produs in lista dupa pozitie ,
# daca adaugam un nr mai mare decat lista, se va adauga la sfarsit
print(category)
category.remove(
    "Comedy"
)  # stergere element din lista dupa denumire doar o singura data
category2.pop(1)  # sterge element dupa pozitie nu dupa denumire
print(category2)
print(category)
print(category.index("Mystery"))  # identificare pozitie in lista a elementului
print(category.count("Mystery"))  # de cate ori apare in lista elementul
category.clear()  # elimina toate elementele din lista
print(category)
category3 = ["casa", "masa", "scaun", "perdea"]
## print(category3.extend([1, 5, 2, 42]))
category3.sort()  # nu va putea sa sorteze intre int si strg
category3.sort(reverse=True)  # inversare lista
print(category3)
category.remove("Comedy")  # elminare element din lista
# LISTE- OPERATORI "in" 2.8 si 2.9

cart = ["Laptop", "Mouse"]
cart.append("Mouse")
print(cart)


customers = ["Bob", "Anna", "Joe", "Bob", "Nick"]
for client in customers:
    if client == "Bob":
        print(True)
        break  # fara break va gasi toate elementele "Bob". cu break va face doar o intineratie

print(
    "Bob" in client
)  # varianta mai scurta fara for si in de mai sus - va gasi doar o singura data


customers = ["Bob", "Anna", "Joe", "Bob", "Nick"]
if "Bob" in customers:
    print("Bob is our customer")
else:
    print("Sorry")
