import random


class Person:
    def __init__(self, firstName, lastName, age):
        # public properties
        self.firstName = firstName
        self.lastName = lastName
        # protected properties
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
        # apelat cu class si nu cu obiectul "person1/self"

    def simpleMethodForClass():
        print("simple method() s-a executat!")
        # apelat cu obiectul, si nu cu class
        # instance method

    def simpleMethodForObject(self):
        print("simple method() s-a executat!")

    # static method - se poate apela si cu ajutorul obiectul nu numai cu clasa.
    # apelat cu clasa, dar si cu obiectul (nu ar trebui)
    # Nu pot folosi self. ca parametru.
    @staticmethod
    def simpleMethodForStatic():
        print("simple method() s-a executat!")


Person.simpleMethodForClass()
person1 = Person("Alex", "Popescu", 25)
person1.simpleMethodForObject()
person1.simpleMethodForStatic


# person1-obiectul , Person - clasa
