# list =[]/list()
# tupla=(())/tuple()
# set={}/set()
# frozenset= frozenset()
# dict={cheie:valoare}/dict()


bookDict = {
    "author": "Eric Matthes",
    "title": "Python Crash Course",
    "price": 14.43,
    "reading age": "12 years and up",
    "language": "English",
}

# myDict7 = dict(firstName = 'Joe', lastName = 'Smith')
# print(myDict7)  #{'firstName': 'Joe', 'lastName': 'Smith'}
# myDict3 = dict([("a", 111), ("b", 222)])
# print(myDict3)
# myDict4 = dict([["a", 111], ["b", 222]])
# print(myDict4)
# myDict5 = dict(['qw', 'er', 'ty'])
# print(myDict5)  #{'q': 'w', 'e': 'r', 't': 'y'}

# keyList = ['a','b']
# valueList = [111, 222]
# myDict6 = dict(zip(keyList, valueList))
# print(myDict6)  #{'a': 111, 'b': 222}


# print(productsDict)

# bookDict = {'author': 'Eric Matthes',
#         'title': 'Python Crash Course',
#         'price': 14.43,
#         'reading age': '12 years and up',
#         'language': 'English'
# }
#  print(len(bookDict))  #5 numar pereche cheie valoare.
#######################################comanda zip###############
# productList=["Apa", "Cafea"]
# priceList=[5,7]
# productsDict=dict(zip(productList,priceList))
################################################################

# tupleProducts="produs1", "produs2"
# print(tupleProducts[1])

####acces cheie din dictionar
# myDict1 = {"key1": 1, "key2": 20.5, "key3": True}
# print(myDict1["key1"])  # 1
# bookDict = {
#     "author": "Eric Matthes",
#     "title": "Python Crash Course",
#     "price": 14.43,
#     "reading age": "12 years and up",
#     "language": "English",
# }
# print(bookDict["author"])  # Eric Matthes

# ############cautare daca elementul este in dictionar$$$$$$$
# bookDict = {
#     "author": "Eric Matthes",
#     "title": "Python Crash Course",
#     "price": 14.43,
#     "reading age": "12 years and up",
#     "language": "English",
# }
# infoType = input("What info do you want to know about the book?")
# if infoType in bookDict:
#         print(bookDict[infoType])
# else:
#         print("Sorry!")
# ##############################################$$$$$$$$$$$$$$

# for dictKey, dicVal in bookDict.items():
#     print("{}:{}".format(dictKey, dicVal))
# bookDict['pagesN'] = 350 - adauga pages
# bookDict['author'] = "Test" #modifica autorul
# for dictKey, dicVal in bookDict.items():
#     print("{}:{}".format(dictKey, dicVal))
#############################################################comanda get
######################comanda get############################comanda get
bookDict = {
    "author": "Eric Matthes",
    "title": "Python Crash Course",
    "price": 14.43,
    "reading age": "12 years and up",
    "language": "English",
}
print(bookDict.get("author"))  # Eric Matthes
print(bookDict.get("page"))  # None
print(bookDict.get("page", 0))  # 0
print(bookDict.get("page", "Elementul nu exista"))

# ##############alipire doua dictionare comanda update&&&&&&&&&&
# studGr1 = {'Joe':75, 'Bob':92}
# studGr2 = {'Kate':62, 'Joe':90, 'Jack':84}
# print(studGr1) #{'Joe': 75, 'Bob': 92}
# studGr1.update(studGr2)
# print(studGr1) #{'Joe': 90, 'Bob': 92, 'Kate': 62, 'Jack': 84}
###########################################################

###################CLEAR goleste dictionarul si functia DEL sterge dictionarul

# ################ Comanda KEYS printeaza toate cheile din dictionar
# bookDict = {
#     "author": "Eric Matthes",
#     "title": "Python Crash Course",
#     "price": 14.43,
#     "reading age": "12 years and up",
#     "language": "English",
# }
# print(bookDict.keys())
# # dict_keys(['author', 'title', 'price', 'reading age', 'language'])
# keyList = list(bookDict.keys())
# print(keyList)  # ['author', 'title', 'price', 'reading age', 'language']


# #########################comanda .values returneaza valorile

# valuesList = list(bookDict.values())
# print(valuesList)
# # ['Eric Matthes', 'Python Crash Course', 14.43, '12 years and up', 'English']


# ################################# comanda .items returneaza tot dictionarul in
# #  tuple cu cheile si valorile lor

# dictItems = list(bookDict.items())
# print(dictItems)

# ##################################################comanda .pop elimina o cheie din dictionar
# # si inlocuieste

# delItem = bookDict.pop("price")
# print("item {} was deleted".format(delItem))
# print(bookDict)
# delItem = bookDict.pop("discount", "None")
# print(delItem)

# # delItem = bookDict.pop("discount") - va da eroare daca nu exista cheia in dictionar

# for dictKey in bookDict:
#     print(bookDict[dictKey])

# for dictKey in bookDict:
#     print("{}:{}".format(dictKey, bookDict[dictKey]))

# # print(bookDict.items())
# # for dictkey, dictVal in bookDict.items()
# #     print (bookDict)
