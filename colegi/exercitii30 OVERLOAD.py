# Task 1
# Supplement the Human class with a constructor, as well as the required overloaded methods.


class Human:
    def __init__(self, nume, varsta):
        self.nume = nume
        self.varsta = varsta

    def __str__(self):
        return f"Nume: {self.nume}, Varsta: {self.varsta}"

    def __eq__(self, other):
        if isinstance(other, Human):
            return self.nume == other.nume and self.varsta == other.varsta
        return False

    def __lt__(self, other):
        if isinstance(other, Human):
            return self.varsta < other.varsta
        return NotImplemented


if __name__ == "__main__":
    human1 = Human("Ion", 25)
    human2 = Human("Maria", 30)
    human3 = Human("Ion", 25)

    print(human1)
    print(human1 == human2)
    print(human1 == human3)
    print(human1 < human2)
# Task 2
# Supplement the City class with a constructor, as well as the required overloaded methods.


class City:
    def __init__(self, nume, populatie):
        self.nume = nume
        self.populatie = populatie

    def __str__(self):
        return f"Nume: {self.nume}, Populatie: {self.populatie}"

    def __eq__(self, other):
        if isinstance(other, City):
            return self.nume == other.nume and self.populatie == other.populatie
        return False

    def __lt__(self, other):
        if isinstance(other, City):
            return self.populatie < other.populatie
        return NotImplemented


if __name__ == "__main__":
    city1 = City("Bucuresti", 1800000)
    city2 = City("Timisoara", 300000)
    city3 = City("Bucuresti", 1800000)

    print(city1)
    print(city1 == city2)
    print(city1 == city3)
    print(city1 < city2)

# Task 3
# Supplement the Country class with a constructor, as well as the required overloaded methods.


class Country:
    def __init__(self, nume, populatie, suprafata):
        self.nume = nume
        self.populatie = populatie
        self.suprafata = suprafata

    def __str__(self):
        return f"Nume: {self.nume}, Populatie: {self.populatie}, Suprafata: {self.suprafata}"

    def __eq__(self, other):
        if isinstance(other, Country):
            return (
                self.nume == other.nume
                and self.populatie == other.populatie
                and self.suprafata == other.suprafata
            )
        return False

    def __lt__(self, other):
        if isinstance(other, Country):
            densitate_self = self.populatie / self.suprafata
            densitate_other = other.populatie / other.suprafata
            return densitate_self < densitate_other
        return NotImplemented


if __name__ == "__main__":
    country1 = Country("Romania", 20000000, 300000)
    country2 = Country("Spania", 50000000, 500000)
    country3 = Country("Romania", 20000000, 300000)

    print(country1)
    print(country1 == country2)
    print(country1 == country3)
    print(country1 < country2)

# Task 4
# Supplement the Fraction class with a constructor, as well as the required overloaded methods.


class Fraction:
    def __init__(self, numarator, numitor):
        if numitor == 0:
            raise ValueError("Numitorul nu poate fi zero")
        self.numarator = numarator
        self.numitor = numitor
        self._simplifica()

    def _simplifica(self):
        from math import gcd

        divizor = gcd(self.numarator, self.numitor)
        self.numarator //= divizor
        self.numitor //= divizor

    def __str__(self):
        return f"{self.numarator}/{self.numitor}"

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.numarator == other.numarator and self.numitor == other.numitor
        return False

    def __add__(self, other):
        if isinstance(other, Fraction):
            numarator = self.numarator * other.numitor + other.numarator * self.numitor
            numitor = self.numitor * other.numitor
            return Fraction(numarator, numitor)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self.numarator * other.numitor < other.numarator * self.numitor
        return NotImplemented


if __name__ == "__main__":
    fraction1 = Fraction(1, 2)
    fraction2 = Fraction(1, 3)
    fraction3 = Fraction(1, 2)

    print(fraction1)
    print(fraction1 == fraction2)
    print(fraction1 == fraction3)
    print(fraction1 < fraction2)
    print(fraction1 + fraction2)
# Task 5
# Implement a class Clock. Store the following in it: power type, manufacturer, year of manufacture, price, type
# (digital, tabletop, wall, regulator, etc.) Implement a constructor and class methods to input and output data, as well as other operations. Use method overloading.


class Clock:
    def __init__(self, power_type, manufacturer, year, price, clock_type):
        self.power_type = power_type
        self.manufacturer = manufacturer
        self.year = year
        self.price = price
        self.clock_type = clock_type

    def display(self):
        print(f"Power Type: {self.power_type}")
        print(f"Manufacturer: {self.manufacturer}")
        print(f"Year of Manufacture: {self.year}")
        print(f"Price: {self.price}")
        print(f"Clock Type: {self.clock_type}")

    def input_data(self):
        self.power_type = input("Enter power type: ")
        self.manufacturer = input("Enter manufacturer: ")
        self.year = int(input("Enter year of manufacture: "))
        self.price = float(input("Enter price: "))
        self.clock_type = input("Enter clock type: ")

    def __str__(self):
        return f"Clock: {self.manufacturer} - {self.power_type} - {self.year} - {self.price} - {self.clock_type}"

    def __eq__(self, other):
        if isinstance(other, Clock):
            return (
                self.manufacturer == other.manufacturer
                and self.year == other.year
                and self.clock_type == other.clock_type
            )
        return False

    def __lt__(self, other):
        if isinstance(other, Clock):
            return self.price < other.price
        return NotImplemented

    def set_price(self, price=None, discount=None):
        if price is not None:
            self.price = price
        elif discount is not None:
            self.price = self.price * (1 - discount / 100)
        else:
            raise ValueError("Either price or discount must be provided")


if __name__ == "__main__":
    c1 = Clock("Battery", "Rolex", 2020, 1000, "Digital")
    c2 = Clock("Mechanical", "Seiko", 2018, 1200, "Wall")
    c3 = Clock("Battery", "Rolex", 2020, 1000, "Digital")

    c1.display()
    c2.display()

    print(c1 == c2)
    print(c1 == c3)
    print(c1 < c2)

    c2.set_price(discount=10)
    print(f"Pret nou pentru {c2.manufacturer}: {c2.price} lei")

# Task 6

# Implement a class Website. Store the following in it: website name, address, description. Implement a constructor and class methods to
# input and output data, as well as other operations. Use method overloading.


class Website:
    def __init__(self, nume, adresa, descriere):
        self.nume = nume
        self.adresa = adresa
        self.descriere = descriere

    def display(self):
        print("informatii website")
        print(f"Nume: {self.nume}")
        print(f"Adresa: {self.adresa}")
        print(f"Descriere: {self.descriere}")

    def input_data(self):
        self.nume = input("Introduceti numele website-ului: ")
        self.descriere = input("Introduceti descrierea site-ului: ")
        self.adresa = input("Introduceti adresa site-ului: ")

    def __str__(self):
        return f"Website: {self.nume} - {self.adresa} - {self.descriere}"

    def __eq__(self, other):
        if isinstance(other, Website):
            return self.adresa == other.adresa
        return False

    def __lt__(self, other):
        if isinstance(other, Website):
            return len(self.nume.lower()) < len(other.nume.lower())
        return NotImplemented

    def update(self, nume=None, adresa=None, descriere=None):
        if nume is not None:
            self.nume = nume
        if adresa is not None:
            self.adresa = adresa
        if descriere is not None:
            self.descriere = descriere


if __name__ == "__main__":
    w1 = Website("Facebook", "https://www.facebook.com/", "Retea de socializare")
    w2 = Website("GitHub", "https://github.com", "Platforma pentru host")
    w3 = Website("Facebook", "https://www.facebook.com/", "Retea de socializare")

    w1.display()
    w2.display()

    print(w1 == w2)
    print(w1 == w3)
    print(w1 < w2)

    w1.update(descriere="Noua descriere pentru site 1")
    w1.display()
