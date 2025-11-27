# Topic: Multiple Inheritance. Polymorphism. Using Magic Method.
# Task 1
# Create a base class Shape with a method for calculating the area.
# Create derived classes: a rectangle, circle, right triangle,
#  trapezoid with their own methods for calculating the area.


# Task 2
# Override the int (returns the area) and str (returns info about a shape)
# methods from Task 1.


import math

# TASK 1 ###########################################
# class Shape:
#     def area(self):
#         """Polymorphic method that must be overridden."""
#         raise NotImplementedError("Subclasses must implement the area method")


# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height


# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * self.radius**2

# class RightTriangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height

#     def area(self):
#         return (self.base * self.height) / 2


# class Trapezoid(Shape):
#     def __init__(self, base1, base2, height):
#         self.base1 = base1
#         self.base2 = base2
#         self.height = height

#     def area(self):
#         return (self.base1 + self.base2) * self.height / 2
########################################################################
# TASK 2


class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement the area method")

    def __int__(self):
        return int(self.area())

    def __str__(self):
        return f"Shape with area: {self.area()}"


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return (
            f"Rectangle(width={self.width}, height={self.height}, area={self.area()})"
        )


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def __str__(self):
        return f"Circle(radius={self.radius}, area={self.area():.2f})"


class RightTriangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height / 2

    def __str__(self):
        return (
            f"RightTriangle(base={self.base}, height={self.height}, area={self.area()})"
        )


class Trapezoid(Shape):
    def __init__(self, base1, base2, height):
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def area(self):
        return (self.base1 + self.base2) * self.height / 2

    def __str__(self):
        return f"Trapezoid(base1={self.base1}, base2={self.base2}, height={self.height}, area={self.area()})"


# Rulare Task 1 si Task 2
shapes = [Rectangle(4, 5), Circle(3), RightTriangle(6, 8), Trapezoid(3, 7, 4)]

for s in shapes:
    print(s)
    print("Area as int:", int(s))
    print()

####################################
# Moștenire simplă
# Toate clasele derivă din Shape.
# Polimorfism
# Metoda area() este apelată diferit în funcție de tipul obiectului.
# Magic Methods
# __int__ → transformă forma în aria ei (int)
# __str__ → furnizează o descriere frumoasă
# Principiul OOP: Open for extension
# Poți adăuga alte forme fără să modifici clasa Shape.
###################################
