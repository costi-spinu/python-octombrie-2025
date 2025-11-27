# Topic: Operator Overloading. Part 5
# Task 1
# Create a Circle class. Implement the following overloaded operators:
# •	Check if radii of two circles are equal (the == operator);
# •	Compare the lengths of two circles (the operators: >, <, <=, >=);
# •	Proportionally change the circle size by changing its radius (the operators: +, -, +=, -=).


import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f"Raza cercului este:{self.radius:.2f}"

    def __eq__(self, value):  # verificare egalitate
        if isinstance(value, Circle):
            return self.radius == value.radius
        return NotImplemented

    def circumferintacerc(self):
        return 2 * math.pi * self.radius

    def __lt__(self, value):
        if isinstance(value, Circle):
            return self.circumferintacerc() < value.circumferintacerc()
        return NotImplemented

    def __le__(self, value):
        if isinstance(value, Circle):
            return self.circumferintacerc() <= value.circumferintacerc()
        return NotImplemented

    def __gt__(self, value):
        if isinstance(value, Circle):
            return self.circumferintacerc() > value.circumferintacerc()
        return NotImplemented

    def __ge__(self, value):
        if isinstance(value, Circle):
            return self.circumferintacerc() >= value.circumferintacerc()
        return NotImplemented

    def __add__(self, value):
        if isinstance(value, (int, float)):
            return Circle(self.radius + value)
        return NotImplemented

    def __sub__(self, value):
        if isinstance(value, (int, float)):
            return Circle(self.radius - value if self.radius - value > 0 else 0)
        return NotImplemented

    def __iadd__(self, value):
        if isinstance(value, (int, float)):
            self.radius += value
            return self
        return NotImplemented

    def __isub__(self, value):
        if isinstance(value, (int, float)):
            self.radius = max(0, self.radius - value)
            return self
        return NotImplemented


# rulare
if __name__ == "__main__":
    c1 = Circle(5)
    c2 = Circle(7)
    c3 = Circle(5)

    print(c1 == c3)
    print(c1 < c2)
    print(c1 > c2)

    c4 = c1 + 3
    print(c4)

    c1 += 2
    print(c1)

    c2 -= 4
    print(c2)

# Explicatii:
#####################################################################
# __eq__ → checks if the radii of two circles are equal.
# __lt__, __le__, __gt__, __ge__ → compare circles by their circumference (2πr).
# __add__, __sub__ → return a new circle with an adjusted radius.
# __iadd__, __isub__ → modify the radius in place (for += and -=).
# Radius never becomes negative (automatically limited to 0).
#####################################################################


# Task 2
# Create a Complex class (complex number). Here is a detailed description of what a
# complex number is: Complex number.
# Create operator overloading for arithmetic operations for working with complex
# numbers (the operators: +, -, *, /).


class Complex:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __str__(self):
        sign = "+" if self.imag >= 0 else "-"
        return f"{self.real} {sign} {abs(self.imag)}i"

    # Metoda magica - adunare
    def __add__(self, value):
        if isinstance(value, Complex):
            return Complex(self.real + value.real, self.imag + value.imag)
        return NotImplemented

    # Metoda magica - scadere
    def __sub__(self, value):
        if isinstance(value, Complex):
            return Complex(self.real - value.real, self.imag - value.imag)
        return NotImplemented

    # Metoda magica - inmultire
    def __mul__(self, value):
        if isinstance(value, Complex):
            real = self.real * value.real - self.imag * value.imag
            imag = self.real * value.imag + self.imag * value.real
            return Complex(real, imag)
        return NotImplemented

    # Metoda magica - impartire
    def __truediv__(self, value):
        if isinstance(value, Complex):
            denominator = value.real**2 + value.imag**2
            if denominator == 0:
                raise ZeroDivisionError("Division by zero complex number")

            real = (self.real * value.real + self.imag * value.imag) / denominator
            imag = (self.imag * value.real - self.real * value.imag) / denominator
            return Complex(real, imag)
        return NotImplemented


# Example usage:
if __name__ == "__main__":
    c1 = Complex(3, 4)
    c2 = Complex(1, -2)

    print("c1 =", c1)
    print("c2 =", c2)
    print("c1 + c2 =", c1 + c2)
    print("c1 - c2 =", c1 - c2)
    print("c1 * c2 =", c1 * c2)
    print("c1 / c2 =", c1 / c2)


# Task 3
# Create an Airplane class. Implement the following using the operator overloading:
# •	Check if the airplane types are equal (the == operator);
# •	Increasing and decreasing the number of passengers in the cabin (the operators: +, -, +=, -=);
# •	Compare two airplanes for the maximum possible number of passengers on
# board (the operators: >, <, <=, >=).


class Airplane:
    def __init__(self, airplane_type: str, max_passengers: int, passengers: int = 0):
        self.airplane_type = airplane_type  # tipul avionului (ex: "Boeing 737")
        self.max_passengers = max_passengers  # capacitatea maximă
        self.passengers = passengers  # număr curent de pasageri

    def __str__(self):
        return (
            f"Airplane(type={self.airplane_type}, "
            f"passengers={self.passengers}, max={self.max_passengers})"
        )

    # ==  → tipurile de avion sunt egale?
    def __eq__(self, other):
        if isinstance(other, Airplane):
            return self.airplane_type == other.airplane_type
        return NotImplemented

    # Comparare după capacitatea maximă de pasageri
    def __lt__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers < other.max_passengers
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers <= other.max_passengers
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers > other.max_passengers
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers >= other.max_passengers
        return NotImplemented

    # + și -  → modifică numărul de pasageri (returnează UN NOU obiect)
    def __add__(self, value):
        if isinstance(value, int):
            new_passengers = self.passengers + value
            # limităm între 0 și capacitatea maximă
            new_passengers = max(0, min(self.max_passengers, new_passengers))
            return Airplane(self.airplane_type, self.max_passengers, new_passengers)
        return NotImplemented

    def __sub__(self, value):
        if isinstance(value, int):
            new_passengers = self.passengers - value
            new_passengers = max(0, min(self.max_passengers, new_passengers))
            return Airplane(self.airplane_type, self.max_passengers, new_passengers)
        return NotImplemented

    # += și -=  → modifică numărul de pasageri IN PLACE (același obiect)
    def __iadd__(self, value):
        if isinstance(value, int):
            self.passengers += value
            self.passengers = max(0, min(self.max_passengers, self.passengers))
            return self
        return NotImplemented

    def __isub__(self, value):
        if isinstance(value, int):
            self.passengers -= value
            self.passengers = max(0, min(self.max_passengers, self.passengers))
            return self
        return NotImplemented


# Exemplu de utilizare
if __name__ == "__main__":
    a1 = Airplane("Boeing 737", max_passengers=180, passengers=50)
    a2 = Airplane("Airbus A320", max_passengers=150, passengers=80)
    a3 = Airplane("Boeing 737", max_passengers=200, passengers=10)

    # 1) Egalitate de tip
    print(a1 == a3)  # True (ambele sunt "Boeing 737")
    print(a1 == a2)  # False

    # 2) Comparare după capacitatea maximă
    print(a1 > a2)  # True (180 > 150)
    print(a2 <= a3)  # True (150 <= 200)

    # 3) Modificare număr de pasageri cu +, -, +=, -=
    a4 = a1 + 100  # creează un nou avion cu mai mulți pasageri
    print(a4)  # pasagerii sunt limitați la max_passengers

    a5 = a2 - 50
    print(a5)

    a1 += 200  # modifică direct a1 (nu poate trece de max_passengers)
    print(a1)

    a2 -= 200  # nu scade sub 0
    print(a2)


# Task 4
# Create an Apartment class. Implement the following overloaded operators:
# •	Check if the areas of the apartments are equal (the == operator);
# •	Check if the areas of the apartments are not equal (the != operator);
# •	Compare the prices of two apartments (the operators: >).


class Apartment:
    def __init__(self, area: float, price: float):
        self.area = area  # suprafața apartamentului în m²
        self.price = price  # prețul apartamentului

    def __str__(self):
        return f"Apartment(area={self.area} m², price={self.price} €)"

    # ==  → verifică dacă două apartamente au aceeași suprafață
    def __eq__(self, other):
        if isinstance(other, Apartment):
            return self.area == other.area
        return NotImplemented

    # != → opusul lui ==
    def __ne__(self, other):
        if isinstance(other, Apartment):
            return self.area != other.area
        return NotImplemented

    # > → compară două apartamente după preț
    def __gt__(self, other):
        if isinstance(other, Apartment):
            return self.price > other.price
        return NotImplemented


# Rulare program
if __name__ == "__main__":
    ap1 = Apartment(60, 80_000)
    ap2 = Apartment(75, 100_000)
    ap3 = Apartment(60, 70_000)

    print(ap1 == ap3)  # True (suprafețele sunt egale)
    print(ap1 != ap2)  # True
    print(ap2 > ap1)  # True (100000 > 80000)

    print(ap1)
    print(ap2)
