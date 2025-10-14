# #TUPLES (listă imuabilă- nemodificabila)

##1.1. Collections of Immutable Objects
# userTypes = ["admin", "student", "teacher"]
# userTypes[0] = "user"
# print (userTypes)

#######1.2. Application and Features of Tuple

# myEmptyTuple1 = ()
# myEmptyTuple2 = tuple() ## functia tuple

# print(myEmptyTuple1)
# print(type(myEmptyTuple1))
# print(myEmptyTuple1)
# print(type(myEmptyTuple2))

# myTuple1 = ('element1', 12, 35.6, False)
# myTuple2 = ('item1')
# userTypes = 'admin', 'student', 'teacher'
# userName = 'Jane',
# print("myTuple1:", myTuple1, "type: ", type(myTuple1))
# print("myTuple2:", myTuple2, "type: ", type(myTuple2))
# print("userTypes:", userTypes, "type: ", type(userTypes))
# print("userName:", userName, "type: ", type(userName))


# itemTuple = ('item1', 'item2', 'item1', 'item3') # valori multiplicate
# print(itemTuple) #('item1', 'item2', 'item1', 'item3')

# namesTuple = tuple(('Alex', 'Helen'))
# print(namesTuple) #('Alex', 'Helen')

################ tupleOfList=tuple([1,2,3], [4,5,6,],[7,8,9])
# print(tupleOfList) #TypeError: tuple expected at most 1 argument, got 3
# tupleOfList = tuple(
#     (
#         [1, 2, 3],
#         [
#             4,
#             5,
#             6,
#         ],
#         [7, 8, 9],
#     )
# )  # - se pun doua paranteze
# print(tupleOfList)  # ([1, 2, 3], [4, 5, 6], [7, 8, 9])


# # # #Negative indexing is also possible.
# userTypes = ("admin", "student", "teacher", "moderator")
# # print("1st user:", userTypes[0])
# # print("last user:", userTypes[len(userTypes) - 1])
# # print("last user once again:", userTypes[-1])


# print("1st two users:", userTypes[::2])
# print("1st two users:", userTypes[:2])
# print(
#     "2nd and 3rd users:", userTypes[1:3]
# porneste de la 1 si se termina la 3 , fara 3

################################## slice(start,end,step)


## nu se pot modifica valorile din tuplu
# userTypes = ('admin', 'student', 'teacher', 'moderator')
# userTypes[0] = 'user' ##'tuple' object does not support item assignment
##comanda del tupleName - sterge intregul tuple , dar nu se pot elimina valori din tuple.


######## creare lista din tuple
# userTypes = ("admin", "student", "teacher", "moderator")
# # userTypesList=['admin', 'student', 'teacher', 'moderator']
# # creare lista goala for , for (in tuple)
# userTypesList = list(userTypes)
# userTypesList[0] = "user"
# userTypesTuple = tuple(userTypesList)
# print(userTypesList)
# print(userTypesTuple)


##### DESPACHETARE IN VARIABILE

# userTypes = ("admin", "student", "teacher", "moderator")
# user1, user2, user3, user4 = userTypes
# user5 = userTypes[0]
# userTypes = ["admin", "student", "teacher", "moderator"]
# user1, user2, user3, user4 = userTypes
# print(user1)  # admin
# print(user2)  # student
# print(user3)  # teacher
# print(user4)  # moderator


# userTypes = ("admin", "student", "teacher", "moderator")
# user1, *users = userTypes
# print(user1)  # admin
# print(users)  # ['student', 'teacher', 'moderator']


# userTypes = ("admin", "student", "teacher", "moderator")
# firstUser, *users, lastUser = userTypes
# print(firstUser)  # admin
# print(users)  # ['student', 'teacher']
# print(lastUser)  # moderator


# userTypes = ("admin", "student", "teacher", "moderator")
# for user in userTypes:
#     print(user)


# userTypes = ('admin', 'student', 'teacher', 'moderator')
# for i in range(len(userTypes)):
#     print(userTypes[i])

userTypes1 = ('admin', 'student', 'teacher', 'moderator')
userTypes2 = ('user1', 'user2')
allUsers = userTypes1 + userTypes2 ################## alipire
print(allUsers)
for user in allUsers:
    print(user)

# userTypes = ("admin", "student", "teacher", "moderator")
# for user in userTypes * 2:  ##########duplicare
#     print(user)
