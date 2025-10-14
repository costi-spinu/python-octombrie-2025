######################## numarare elemente
# userTypes = ('admin', 'student', 'teacher', 'moderator', 'admin')
# print(userTypes.count('admin'))  #2 numara
######################## identificare un anumit element si pozitia lui pe index
# userTypes = ('admin', 'student', 'teacher', 'moderator', 'admin')
# print(userTypes.index('admin')) #0 transmite doar prima pozitie

######################## cautare element in tupla
# userTypes = ('admin', 'student', 'teacher', 'moderator', 'admin')
# if 'student' in userTypes:
#     print('student is correct login' )

####################### functia def - creare tupla


def askPersonalInfo():
    while True:
        firstName = input("Input your first name:")
        lastName = input("Input your last name:")
        yearBirth = input("Input your year of birth:")
        gender = input("Input your gender (M, F):")
        if (
            firstName == ""
            or lastName == ""
            or yearBirth == ""
            or gender == ""
            or gender not in ("F", "M")
        ):
            print("Wrong data!")
        else:
            return firstName, lastName, yearBirth, gender


personalInfo = askPersonalInfo()
print(personalInfo)


#############################
## We also used the ('F', 'M')
# tuple to verify the entered a
# valid value by the user for the
# "gender" information.
#############################


# def askHobby():
#     hobbyInd = 1
#     hobbyList = []
#     while True:
#         hobbyName = input("Name of the hobby #{}:".format(hobbyInd))
#         if hobbyName == "":
#             print("No info. Input stopped.")
#             break
#         else:
#             hobbyList.append(hobbyName)
#             hobbyInd += 1
#     if len(hobbyList) > 0:
#         print("You have {} hobbies.".format(hobbyInd - 1))
#     else:
#         print("You have no hobbies at all")
#     return hobbyList


# askHobby = askHobby()
# print(askHobby)

###############################
# Now let's make it more universal so that
#  it can also be used to form a list of
# programming languages that the user knows:
# for this, we will pass part of the query
# string ("hobby", "programming languages")
# as a parameter to our function. We will
# also make the names of its local variables
# more universal.
###################################


# def askPersonalInfo():
#     while True:
#         firstName = input("Your first name:")
#         lastName = input("Your last name:")
#         yearBirth = input("Your year of birth:")
#         gender = input("Your gender (M,F):")
#         if (
#             firstName == ""
#             or lastName == ""
#             or yearBirth == ""
#             or gender == ""
#             or gender not in ("F", "M")
#         ):
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
#         if queryStr == "hobby":
#             print("You have {} hobbies.".format(infoInd - 1))
#         elif queryStr == "programming languages":
#             print("You know {} programming languages.".format(infoInd - 1))

#     else:
#         print("You have no info at all")
#     return infoList


# userInfo = []
# userInfo.append(askPersonalInfo())
# userInfo.append(askAdditionalInfo("hobby"))
# userInfo.append(askAdditionalInfo("programming languages"))
# print(userInfo)


# ###########################################################

# listaElemente = [(1, 2, 3), (1, 2, 3)]


#############################################################
# def functieInmultireCu2(numar: int):
#     return numar + numar
#     numar * 3


# numarAdunat = functieInmultireCu2(9)
# print(numarAdunat)


def verificaNumarContract(numarcontract: int):
    if numarcontract.is_integer():
        print("Este numarul de contract bun!")
    else:
        ValueError("Nu este un numar de contract bun")


verificareaNumaruluideContract = verificaNumarContract(5)
print(verificareaNumaruluideContract)  # NONE
