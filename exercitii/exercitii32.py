# Task 1
# Add a static method to the Human
# class that when called returns the
# number of created Human class objects.


class Human:
    count = 0

    def __init__(self, name):
        self.name = name
        Human.count += 1

    @staticmethod
    def get_count():
        return Human.count


h1 = Human("Ana")
h2 = Human("Ion")


print(Human.get_count())

# Task 2
# Create a class to calculate the area
# of geometric shapes. The class should
# provide functionality for calculating the
# area of a triangle using various formulas,
# the area of a rectangle, the area of a square,
#  the area of a rhombus. Class methods for
# calculating the area should be implemented
# with static methods. The class should also
# count the number of calculations and return
# that value using a static method.

import math


class Geometrie:
    calcul = 0

    @staticmethod
    def arietriunghi(baza, inaltime):
        Geometrie.calcul += 1
        return 0.5 * baza * inaltime

    @staticmethod
    def ariedreptunghi(lungime, latime):
        Geometrie.calcul += 1
        return lungime * latime

    @staticmethod
    def ariepatrat(l):
        Geometrie.calcul += 1
        return l**2

    @staticmethod
    def arieromb(a, b):
        Geometrie.calcul += 1
        return 0.5 * a * b

    @staticmethod
    def totalcalcule():
        return Geometrie.calcul


print("Aria triunghiului isoscel", Geometrie.arietriunghi(2, 60))
print("Aria dreptunghi", Geometrie.ariedreptunghi(2, 6))
print("Aria patrat", Geometrie.ariepatrat(2))
print("Aria romb:", Geometrie.arieromb(2, 3))
print("Nr total de calcule", Geometrie.totalcalcule())

# Task 3
# Create a class to find the largest and the
# smallest of four arguments, the average, and
# the factorial. Implement this functionality as static methods

import math


class OperatiiMatematice:
    @staticmethod
    def celmaimare(a, b, c, d):
        return max(a, b, c, d)

    @staticmethod
    def celmaimic(a, b, c, d):
        return min(a, b, c, d)

    @staticmethod
    def fractie(a, b, c, d):
        return (a + b + c + d) / 4

    @staticmethod
    def factorial(a):
        return math.factorial(a)


print("Cel mai mare numar", OperatiiMatematice.celmaimare(1, 5, 6, 7))
print("Cel mai mic numar", OperatiiMatematice.celmaimic(1, 6, 7, 2))
print("fractie", OperatiiMatematice.fractie(1, 23, 24, 2))
print("Factorial 10:", OperatiiMatematice.factorial(10))
