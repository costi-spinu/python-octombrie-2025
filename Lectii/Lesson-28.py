# import random
# class Student:
#     spec = "Computer science"

#     def __init__(self, name, age):
#         self.name = name
#         #public property
#         self.age = age
#         #private property
#         self.__personID=random.randint(1,100)

#     def __getPersonID(self):
#         return f"{self.__personID}"

#     def __getPersonIDPublic(self):
#         return f"{self.__getPersonID()}"

#     def showInfo(self):
#         return f"Student {self.name} is {self.age} years old."

#     def showMsg(self, msgText):
#         return f"Student {self.name} says '{msgText}'."


# # student1 = Student("Nume-1", 20)  # obiectul
# # student2 = Student("Nume-2", 20)
# # student3 = Student("Nume-3", 20)
# # student4 = Student("Nume-4", 20)
# student1 = Student("Bob", 20)
# # student2 = Student("Jane", 18)
# # print(type(student1))
# # print(student1.age)
# # print(student1.showInfo())
# # print(student1.showMsg("Hello!"))
# # print(student2.showInfo())
# # print(student2.showMsg("Hi!"))
# # print(student1.showInfo())
# print (student1.__getPersonIDPublic())


class Person:
    def __init__(self, firstName: str, lastName: str, age: int):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

    def getInfo(self):
        return f"Person first name -  {self.firstName}; last name - {self.lastName}; age - {self.age}."

    def getHi(self, msgText):
        return f"{msgText}! I am {self.firstName}."


personX = Person("Costi", "Spinu", 1)
print(personX.firstName)
print(personX.lastName)
print(personX.age)


class Student(Person):  # mostenire
    spec = "Computer Science"

    def __init__(self, firstName, lastName, age, score):
        super().__init__(firstName, lastName, age)
        self.score = score

    def isSuccessful(self, meanScore):
        return True if meanScore <= 75 else False


student1 = Student("Costi", "Spinu", 36, 100)
print(student1.score)
