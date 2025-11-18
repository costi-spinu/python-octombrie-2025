# Task 3
# Create a Money class for working with money
# (the class object operates with one currency).
# The class must provide a field for storing an integer part
# (dollars, euros, hryvnias, etc.) and a field for storing a
# fractional part (cents, euro cents, kopecks, etc.)
# Implement methods for printing amounts and setting values
# for parts (integer and fractioanl).
# Based on the Money class, create a Product class.
# Implement a method that allows you to decrease the
# price by a specified number.
# Implement methods and fields required for each class.
#


class Bani:
    def __init__(self, parte_intreaga=0, parte_fractionara=0):
        self.parte_intreaga = parte_intreaga  # lei / euro / dolari
        self.parte_fractionara = parte_fractionara % 100
        self.parte_intreaga += parte_fractionara // 100

    def seteaza(self, partea_intreaga, partea_fractionara):
        self.parte_intreaga = partea_intreaga + partea_fractionara // 100
        self.parte_fractionara = partea_fractionara % 100

    def afiseaza(self):
        return f"{self.parte_intreaga}.{self.parte_fractionara:02d}"


class Produs(Bani):
    def __init__(self, nume, parte_intreaga, parte_fractionara):
        super().__init__(parte_intreaga, parte_fractionara)
        self.nume = nume

    def reducere(self, suma_bani):
        """suma_bani = reducerea exprimată în bănuți (ex: 250 = 2.50 lei)"""
        total = self.parte_intreaga * 100 + self.parte_fractionara
        total -= suma_bani

        if total < 0:
            total = 0

        self.parte_intreaga = total // 100
        self.parte_fractionara = total % 100

    def afiseaza_produs(self):
        return f"{self.nume} – {self.afiseaza()} lei"


p = Produs("Paine", 3, 50)
print(p.afiseaza_produs())

p.reducere(100)
print(p.afiseaza_produs())
