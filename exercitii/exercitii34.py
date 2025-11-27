# Task 1
# Create a class Number (or use the one you created earlier).
# The Number class stores one value. Use operator overloading to implement arithmetic
# operations for working with this number (the operators: +, -, *, /).


class Number:
    def __init__(self, v: int):
        self.v = v

    # + operator
    def __add__(self, other):
        if isinstance(other, Number):
            return Number(self.v + other.v)
        return Number(self.v + other)

    # - operator
    def __sub__(self, other):
        if isinstance(other, Number):
            return Number(self.v - other.v)
        return Number(self.v - other)

    # * operator
    def __mul__(self, other):
        if isinstance(other, Number):
            return Number(self.v * other.v)
        return Number(self.v * other)

    # / operator
    def __truediv__(self, other):
        if isinstance(other, Number):  # verifica daca other este tot un obiect Number
            # de exemplu isinstante (3,int) verifica daca 3 este integer. - True
            # isinstance() te ajută să verifici dinamic ce tip are un obiect,
            # pentru a decide cum să îl prelucrezi în cod.
            return Number(self.v / other.v)
        return Number(self.v / other)

    # Representare pentru afisare
    def __repr__(self):
        return f"{self.v}"


a = Number(10)
b = Number(5)


print(a + b)
print(a - b)
print(a * b)
print(a / b)

print(a + 3)  # """Se aplica isinstance"""
print(3 + a.v)
