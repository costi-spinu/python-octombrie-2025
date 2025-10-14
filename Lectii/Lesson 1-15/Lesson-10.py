# name = "Student"
# age = 25
# strMsg3 = "My name is {name}, I'm {age}".format(name=name, age=age)
# print(strMsg3)  # My name is Student, I'm 25
# strMsg4 = "My name is {name}, I'm {age}".format(age=25, name="Student")
# print(strMsg4)  # My name is Student, I'm 25


# # strMsg3_2 = "My name is:" + name + "I'm" + str(age)
# # print(strMsg3_2)


# import re
# userStr = "abcd abc efgh"
# match = re.search(r'\w{4}', userStr)


dummText = (
    "Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
    "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "
    "when an unknown printer took a galley of type and scrambled it to make a type "
    "specimen book. It has survived not only five centuries, but also the leap into "
    "electronic typesetting, remaining essentially unchanged. It was popularised in the "
    "1960s with the release of Letraset sheets "
    "containing Lorem Ipsum passages, and more recently with desktop publishing software "
    "like Aldus PageMaker including versions of Lorem Ipsum."
)

# print(type(dummText))

import re

# match = re.findall("\w{5}", dummText)
# print(match.group())

# listOfStrings = re.findall("Ipsum", dummText)
# num = len(listOfStrings)
# print(num)


# listOfStrings = re.findall(
#     "\w{5}", dummText
# )  # w- caractere alfa-numerice {5} - numarul lor "5"
# print(listOfStrings)


# listOfStrings = re.findall(
#     "\w{5}\b", dummText
# )  # w- caractere alfa-numerice {5} - numarul lor "5" \b - sa nu caute cuvinte care nu au mai mult de 5 litere ----\w{5}\b" - patern
# print(listOfStrings)

lista1 = re.findall(
    r"\b[a-zA-Z]{5}\b", dummText
)  # r"\b[a-zA-Z]{5}\b" - pattern - raw \b inceput si sfarsit de cuvant [a-zA-Z] - literele - {5} - numarul de litere

print(len(lista1))

for elment in lista1:
    print(elment)
