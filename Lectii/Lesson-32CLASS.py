import random
from datetime import date


class Person:
    hobby = "Cooking"
    firstName = "FirstName din clasa"

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

    @staticmethod
    def sayGreetings():
        print("Nice to meet you!")

    # overload
    def methodTest(self, age=20):
        print("Am apelat methodTest si afisez varsta: " + str(age))

    # class methods
    @classmethod
    def setDefaultHobby(cls):
        cls.hobby = "Drawing"

    def setDefaultFirstName(self):
        print("methodSelf->setDefaultFirstName(self)")

    @staticmethod
    def setDefaultFirstName():
        print("@staticmethod->setDefaultFirstName()")

    @classmethod
    def setDefaultFirstName(cls):
        print("@classmethod->setDefaultFirstName()")
        cls.firstName = "Prenume default"

    @classmethod
    def basedOnBYear(cls, firstName, lastName, bYear):
        personAge = date.today().year - bYear
        return cls(firstName, lastName, personAge)


person1 = Person("Alex", "Popescu", 25)
person1.methodTest()
person1.methodTest(35)
# # person2 = Person("Joe", "Black", 30)
# # print(person1.hobby)
# # Person.setDefaultHobby()
# # person3 = Person("Kate", "Smith", 20)
# # print(person2.hobby)
# # person4 = Person("Bob", "Gordon", 40)
# # print(person3.hobby)
# person5 = Person("Joe", "Black", 30)
# person5.setDefaultFirstName()
# print(person5.firstName)
# Person.setDefaultFirstName()
# print(person5.firstName)
# print(Person.firstName)
# print(person5.firstName)
# # --->concluzie: pot sa am 2 proprietati cu denumiri
# # identice(una tine de clasa, cealalta de obiect)
# # --->concluzie metode cu aceeasi denumire: pot avea metode cu aceeasi denumire,
# # dar se vor rescrie->va ramane doar ultima metoda


# # person6=Person()
# print (person6.firstName)

# person1 = Person("Joe", "Black", 30)
# print(person1.getInfo())

# person2 = Person.basedOnBYear("Kate", "Smith", 1989)
# print(person2.getInfo())
