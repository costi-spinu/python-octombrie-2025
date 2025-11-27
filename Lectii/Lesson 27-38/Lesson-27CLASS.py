# class Student:  # clasa sau sablon
#     age = 20
#     name = "Bob"


class Student:
    spec = "Computer science"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def showInfo(self):
        return f"Student {self.name} is {self.age} years old."

    def showMsg(self, msgText):
        return f"Student {self.name} says '{msgText}'."


# student1 = Student("Nume-1", 20)  # obiectul
# student2 = Student("Nume-2", 20)
student3 = Student("Nume-3", 20)
student4 = Student("Nume-4", 20)

student1 = Student("Bob", 20)
student2 = Student("Jane", 18)
print(type(student1))
print(student1.age)
print(student1.showInfo())
print(student1.showMsg("Hello!"))
print(student2.showInfo())
print(student2.showMsg("Hi!"))
