import random
from datetime import date


class Person:
    hobby = "Cooking"
    firstName = "primul din clasa"

    def __init__(self, firstName, lastName, age):
        # public properties
        self.firstName = firstName
        self.lastName = lastName
        # protecte properties
        self._age = age
        # private properties
        self.__personID = random.randint(1, 100)

    # private methods
    def __showID(self):
        print(self.__personID)

    # public methods
    def getInfo(self):
        self.__showID()
        return f"Person first name -  {self.firstName}; last name - {self.lastName}; age - {self._age}."

    def sayHi(self, msgText):
        print(self.getInfo())
        return f"{msgText}! I am {self.firstName}."

    # static methods
    @staticmethod
    def sayGreetings():
        print("Nice to meet you!")

    @classmethod
    def setDefaultHobby(cls):
        cls.hobby = "Drawing"

    @classmethod
    def setDefaultFirstName(cls):
        cls.firstName = "Prenume Default"

    # overload
    def methodTest(self, age=20):
        print("Am apelat methodThest si afisez varsta: " + str(age))


person1 = Person("alex", "Popescu", 25)
person1.methodTest()
person1.methodTest(30)  # s-a facut overload

# person2=Person("Bob", "Gordon",40)
# print(person2.hobby)

person3 = Person("Joe", "Black", 30)
print(person3.firstName)
Person.setDefaultFirstName()
print(person3.firstName)
print(Person.firstName)  # a apelat classmethod cu clasa
print(person3.firstName)
