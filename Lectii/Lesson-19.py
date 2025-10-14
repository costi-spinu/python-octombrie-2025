# def functieTest(a, b):
#     print("def function")
#     counter = 0
#     counter = counter + 1
#     # TODO: bug de rezolvat!
#     if counter == 3:
#         return


# functieTest(1, 2)


# def userGreetings(login="student",passw="111"):
#     if login == 'admin':
#         print("Welcome, admin")
#     elif login == 'student':
#         print("Welcome, student")
#     else:
#         print("Welcome, guy")

# userGreetings("admin", "12345")
# userGreetings("student")
# userGreetings()


# def calculateExample1():
#      baseVar = int(input("input base variable: "))
#      resultVar = baseVar ** 2
#      print(f'The square of {baseVar} is: {resultVar}')

# calculateExample1()
# print(baseVar)

# userName = "Bob"
# print("{} - first user".format(userName))
# def checkUser():
#     global userName
#     userName = "Joe"
#     userLog = input("Input your login: ")
#     if userLog == 'admin':
#         print("{} is admin".format(userName))
#     else:
#         print("{} is user".format(userName))
# checkUser()
# print("{} - second user".format(userName))
counter = 0

def functieTest(a, b):
    print("def function")
    global counter
    counter = counter + 1
    if counter == 3:
        return

    # TODO: bug de rezolvat!
    # def functieTest(a, b):
    #     print("da")

    functieTest(a, b)
    # if counter == 3:
    #     return


functieTest(1, 2)
