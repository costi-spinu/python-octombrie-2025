# def askPersonalInfo():
#     while True:
#         firstName = input("Your first name:")
#         lastName = input("Your last name:")
#         yearBirth = input("Your year of birth:")
#         gender = input("Your gender (M,F):")
#         if firstName == "" or lastName == "" or yearBirth == "" or gender == "" or gender not in ('F','M'):
#             print("Wrong data!")
#         else:
#             return firstName, lastName, yearBirth, gender
# def askAdditionalInfo(queryStr):
#     infoInd = 1
#     infoList = []
#     while True:
#         infoName = input("Name of the {} #{}:".format(queryStr, infoInd))
#         if infoName == "":
#             print("No info. Input stopped.")
#             break
#         else:
#             infoList.append(infoName)
#             infoInd += 1
#     if len(infoList) > 0:
#         if queryStr == 'hobby':
#             print("You have {} hobbies.".format(infoInd - 1))
#         elif queryStr == 'programming languages':
#             print("You know {} programming languages.".format(infoInd-1))

#     else:
#         print("You have no info at all")
#     return infoList
# userInfo = []
# userInfo.append(askPersonalInfo())
# userInfo.append(askAdditionalInfo('hobby'))
# userInfo.append(askAdditionalInfo('programming languages'))
# print(userInfo)

#############SET

# lista1=[1,2,3]
# lista2=list((1,2,3))
# tupla=tuple((1,2,3))

# setx={1,2,3}
# sety=set((1,2,3,4))

######

# passwordsSet={'111',('222','333')} ##trebuie sa fie ceva
#  care nu poate sa fie schimbat - doar tuple - sa le verifice unicitatea
# print(passwordsSet)


# mySetA = {1, 2, 3}
# mySetB = {3, 2, 1}
# print(mySetA == mySetB)  # True


# word = input("Your word:")
# for letter in set(word):
#     print(letter)

################################# adaugare elemente in set
# mySet = {1, 2, 3}
# print(mySet)
# mySet.add(4)
# print(mySet)
# mySet.update([3, 4, 5])
# print(mySet)
# mySet.update([5, 6, 7], {8, 9})
# print(mySet)

################################### stergere elemente din set
# mySet = {1, 2, 3, 4, 5}
# print(mySet)
# mySet.discard(4)
# print(mySet)
# mySet.remove(5)  # daca nu exista elementul primim eroare
# print(mySet)
# mySet.discard(10)  # nu primim eroare
# print(mySet)


################################# uniunea set-urilor si fara repetarea lor

# studGroup1 = {'Hanna', 'Joe', 'Kate'}
# studGroup2 = {'Bob', 'Joe', 'Jane', 'Kate', 'Jack'}
# print("studGroup1:", studGroup1)
# print("studGroup2:", studGroup2)
# print("Intersection of sets:")
# print(studGroup1 & studGroup2) #
# print(studGroup1.intersection(studGroup2))
# print("Union of sets:")
# print(studGroup1studGroup2) #
# print(studGroup1.union(studGroup2))
# print("Difference of two sets:")
# print(studGroup2 - studGroup1) #
# print(studGroup2.difference(studGroup1))

###################################### functiile set-urilor identice cu cele din lista

# enumerate(), len(), max(), min(), sorted(), sum()

################## enumerate()
# studSet = {'Bob', 'Joe', 'Jane', 'Kate', 'Jack'}
# print("We have {} students in our group.".format(len(studSet)))
# for ind, item in enumerate(studSet):
#     print(ind, item)

#################################
#################################
#############FROZEN SET##########

# frozenA = frozenset(["Hanna", "Joe", "Kate"])
# frozenB = frozenset(["Bob", "Joe", "Jane", "Kate", "Jack"])
# print("frozenA:", frozenA)
# print("frozenB:", frozenB)
# print("Intersection of frozensets:")
# print(frozenA & frozenB)
# print(frozenA.intersection(frozenB))
# print("Union of frozensets:")
# # print(frozenAfrozenB)
# print(frozenA.union(frozenB))
# print("Difference of two frozensets:")
# print(frozenB - frozenA)
# print(frozenB.difference(frozenA))


##############2.5. Application of Sets

# allPizzaTypes = ['Veggie', 'Pepperoni', 'Meat', 'Margherita', 'Meat', 'BBQ Chicken', 'Hawaiian', 'Veggie']
# uniquePizzaTypes = list(set(allPizzaTypes))
# print(uniquePizzaTypes)
# ['BBQ Chicken', 'Veggie', 'Meat', 'Margherita', 'Hawaiian', 'Pepperoni']


# word1 = input("1st word:")
# word2 = input("2nd word:")
# if set(word1) == set(word2):
#     print("Yes")
# else:
#     print("No")
