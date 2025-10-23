import random


class Person:
    def __init__(self, firstName, lastName, age):
        # public properties
        self.firstName = firstName
        self.lastName = lastName
        # protected properties
        self._age = age
        self.__personID = random.randint(1, 100)

    # public methods
    def getInfo(self):
        return f"Person first name -  {self.firstName};last name - {self.lastName};age - {self._age}."

    def getHi(self, msgText):
        print(self.getInfo())
        return f"{msgText}! I am {self.firstName}."

    def showPersonID(self):
        print(self.__personID)


class Employee(Person):
    def __init__(self, firstName, lastName, age, salary):
        super().__init__(firstName, lastName, age)
        self.salary = salary

    def isRetiree(self):
        print(self.getInfo())
        if self._age >= 60:
            print(f"{self.firstName} is retiree")
        else:
            print(f"{self.firstName} is not retiree")

    def changeAge(self, newAge):
        self._age = newAge


employee1 = Employee("Joe", "Black", 30, 3000)
employee1.isRetiree()
employee1.changeAge(65)
employee1.isRetiree()
print(employee1.showPersonID())
