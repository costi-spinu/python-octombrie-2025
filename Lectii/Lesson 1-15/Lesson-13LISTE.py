# category = ["Drama", "Comedy", "Mystery", "Romance"]
# for i in range(len(category)):
#     if i == 2:
#         print(
#             "ai o reducere la produsul:" + category[i]
#         )  # adaugare la un produs din lista o referinta

# category.append("Produs nou")  # adaugam un singur element la sfarsitul listei
# print(category)
# category2 = ["casa", "masa"]
# category.extend(
#     category2
# )  # adaugam o lista de elemente (mai multe elemente din alta lista)


##Modificare in variabile
# variabila1 = 10
# variabila2 = variabila1
# variabila2 = 20
# print(variabila1)  # 10
# print(variabila2)  # 20


## Features Lists, links, and Cloning 2.9

# list1 = [1, 2, 3, 4, 5]
# print(list1)

# list2 = list1  # atribuire alt specific listei *nume
# list3 = list2
# print(list2)

# list2[0] = "Hello"
# print(list3)  # [1, 'Hello', 3, 4, 5]
# print(list2)  # [1, 'Hello', 3, 4, 5]
# print(list1)  # [1, 'Hello', 3, 4, 5]


# list1 = [1, 2, 3, 4, 5]
# list2 = list1
# list3 = [1, 2, 3, 4, 5]
# print(list2 is list1)  # True
# print(list3 is list1)  # False
# list4 = list1.copy  # copiaza elemente din lista si le atribuie list4
# print(list4 is list1)
# list5 = list(list1)  # creaza o noua lista cu elementele din list1
# print(list5)
# list4 = list1[:]  # creaza o noua lista cu elementele din list1

# ## cautare elemente
# customers = ['Bob', 'Anna', 'Joe', 'Nick']
# print(customers.index('Joe')) #2
# categoryList = ["Drama", "Comedy", "Mystery", "Romance", "Comedy"]
# print(category.index('Comedy')) #1

# customers = ['Bob', 'Anna', 'Joe', 'Bob', 'Nick']
# for i in range(len(customers)):
#     if customers[i] == 'Bob':
#         print(i)
# #0
# #3

##Matrice

myTbl = [[111, 112, 113], [221, 222, 223]]
print(myTbl[1][1])  # 222
aldoileaelement = myTbl[1]
print(aldoileaelement)
print(aldoileaelement[0])
print(
    myTbl[1][0]
)  ##primul [1] este pentru elementul lista din pozitia 1, si al doilea [0] ia elementul din pozitia 1 din lista identificata
print(myTbl[0])  # [111, 112, 113]


for i in range(2):
    for j in range(3):
        print(myTbl[i][j])
# 111
# 112
# 113
# 221
# 222
# 223


# studScores = [['Bob', 11, 8, 10, 12], ['Jane', 12, 11, 11, 11], ['Kate', 7, 8, 9, 9]]
# # for student in studScores:
# #     print(student)

# for student in studScores:
#     print(student[0],max(student[1:]))


films = [
    ["Catch Me If You Can", "Biography", "Crime", "Drama"],
    ["Mrs. Doubtfire", "Comedy", "Drama", "Family"],
]


# use the copy() function;
# use the list() constructor function;
# use a slice of the entire list [:].


list1 = [1, 2, 3, 4, 5]
print(list1)  # [1, 2, 3, 4, 5]
list2 = list1.copy()
list2[1] = "Hello"
print(list2)  # [1, 'Hello', 3, 4, 5]
print(list1)  # [1, 2, 3, 4, 5]
list3 = list(list1)
list3[2] = "Hello"
print(list3)  # [1, 2, 'Hello', 4, 5]
print(list1)  # [1, 2, 3, 4, 5]
list4 = list1[:]
list4[3] = "Hello"
print(list4)  # [1, 2, 3, 'Hello', 5]
print(list1)  # [1, 2, 3, 4, 5]
