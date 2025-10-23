# Task 1
# Implement a class Human. Class fields should store the
# following: full name, date of birth, contact number, city,
# country, home address. Implement class methods for data input
#  and output, provide access to individual fields through class methods.


# # Task 2
# # Create a class City. Class fields should store the following:
# # city name, region name, country name, number of citizens, zip code,
# # area code. Implement class methods for data input and output, provide
# # access to individual fields through class methods.

# # Task 3
# # Create a class Country. Class fields should store the following:
# # country name, continent, population, calling code, capital, city names.
# # Implement class methods for data input and output, provide access to
# # individual fields through class methods.

# # Task 4
# # Create a class Fraction. Class fields should store the following:
# # numerator and denominator. Implement class methods for data input and output,
# # provide access to individual fields through class methods. Also, create class
# # methods for arithmetic operations (add, subtract, multiply, divide, etc.).


class Human:
    def __init__(
        self,
        nume_prenume: str = "",
        ziua_de_nastere: str = "",
        numar_contact: str = "",
        oras: str = "",
        adresa: str = "",
        CNP: str = "",
    ):
        self.nume_prenume = nume_prenume
        self.ziua_de_nastere = ziua_de_nastere
        self.numar_contact = numar_contact
        self.oras = oras
        self.adresa = adresa

        self.__CNP = CNP

    def introducere_date(self):
        self.nume_prenume = input("Introduceti numele intreg (nume si prenume): ")
        self.ziua_de_nastere = input("Introduceti ziua de nastere (ZZ-LL-AAAA): ")
        self.numar_contact = input("Numar de telefon: ")
        self.oras = input("Oras: ")
        self.adresa = input("Adresa: ")
        self.__CNP = input("Introduceti CNP din 12 cifre: ")

    def get_CNP(self):
        return self.__CNP

    def set_full_CNP(self, CNP):
        self.__CNP = CNP

    def afisare_date(self):
        print(f"\n----- Informatii persoana{i} -----")
        print(f"Nume intreg: {self.nume_prenume}")
        print(f"Ziua de nastere: {self.ziua_de_nastere}")
        print(f"Numar de contact: {self.numar_contact}")
        print(f"Oras: {self.oras}")
        print(f"Adresa: {self.adresa}")
        print(f"CNP:{self.__CNP}")


if __name__ == "__main__":
    persoane = []

    n = int(input("Cate persoane doriti sa introduceti? "))

    for i in range(n):
        print(f"\nIntroduceti datele pentru persoana {i + 1}:")
        persoana = Human()
        persoana.introducere_date()
        persoane.append(persoana)

    print("\n=== Lista de persoane introduse ===")
    for persoana in persoane:
        persoana.afisare_date()
