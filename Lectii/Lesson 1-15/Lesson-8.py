myStr = "Python was created in the late 1980's by Guido van Rossum. Python- cool!"

print(myStr.count("Python"))  # 2
print(myStr.count("Python", 20, 65))  # 1
print(myStr.count("was"))  # 1

# .lower(), .upper(), .title()
# emailUtilizator = input("Adauta email-ul tau:")
# emailUtilizator = emailUtilizator.lower()
# if emailUtilizator == "costispinu@outlook.com":
#     print("Login")
# else:
#     print("Not found!")


# # cautarecuvinte

# myStr = "Python was created in the late 1980's by Guido van Rossum. Python- cool!"
# print(myStr.find("a"))  # 8
# print(myStr.find("a", 2, 5))  # -1


# myStr = "Python was created in the late 1980's by Guido van Rossum. Python- cool!"
# myStr = myStr.lower()
# print(myStr.index("python".lower()))


# myStr = "Python was created in the late 1980's by Guido van Rossum. Python- cool!"

# print(myStr.startswith("P"))  # True
# print(myStr.startswith("p"))  # False
# print(myStr.startswith("w", 7))  # True
# print(myStr.endswith("!"))  # True
# print(myStr.endswith("n", 2, 6))  # True


# myStr = "Python was created in the late 1980's by Guido van Rossum. Python- cool!"

# print(myStr.startswith("P"))  # True
# print(myStr.startswith("p"))  # False
# print(myStr.startswith("w", 7))  # True
# print(myStr.endswith("!"))  # True
# print(myStr.endswith("n", 2, 6))  # True

# myStr = "Python2021"
# print(myStr.isalnum())  # True
# print(myStr.isalpha())  # False

# myAge = "16"
# print(myAge.isdigit())  # True

# myStr1 = "it was created in the late 1980's"
# print(myStr1.islower())  # True

# myStr2 = " \t  \n \t\t"
# print(myStr2.isspace())  # True

# myName1 = "Guido van Rossum"
# print(myName1.istitle())  # False

# myName2 = "GUIDO VAN ROSSUM"
# print(myName2.isupper())  # True


# # aranjare text

myStr = "Python2021"

print(myStr.center(30))
print(myStr.center(30, "*"))
print(myStr.center(5))


# # extragere
myStr = "Python was created in the late 1980's by Guido van Rossum. Python- cool!"
myStr1 = myStr[0:6]
print(myStr1)
myStr2 = myStr[:6]
print(myStr2)
mystr3 = myStr2[:3]
print(mystr3)
