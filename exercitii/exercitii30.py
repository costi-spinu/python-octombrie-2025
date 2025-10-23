# Task 1
# Supplement the Human class with a constructor,
# as well as the required overloaded methods.


# class Human:
#     def __init__(
#         self,
#         nume_prenume: str = "",
#         ziua_de_nastere: str = "",
#         numar_contact: str = "",
#         oras: str = "",
#         adresa: str = "",
#         CNP: str = "",
#     ):
#         self.nume_prenume = nume_prenume
#         self.ziua_de_nastere = ziua_de_nastere
#         self.numar_contact = numar_contact
#         self.oras = oras
#         self.adresa = adresa
#         self.__CNP = CNP  # private attribute

#     # ===== Method 1: Introduce data manually =====
#     def introducere_date(self):
#         self.nume_prenume = input("Introduceti numele intreg (nume si prenume): ")
#         self.ziua_de_nastere = input("Introduceti ziua de nastere (ZZ-LL-AAAA): ")
#         self.numar_contact = input("Numar de telefon: ")
#         self.oras = input("Oras: ")
#         self.adresa = input("Adresa: ")
#         self.__CNP = input("Introduceti CNP din 12 cifre: ")

#     # ===== Method 2: Simulated method overloading =====
#     def set_date(self, *args):
#         """
#         Overloaded version of setting data.
#         1 argument → only nume_prenume
#         3 arguments → nume_prenume, ziua_de_nastere, CNP
#         6 arguments → all fields
#         """
#         if len(args) == 1:
#             self.nume_prenume = args[0]
#         elif len(args) == 3:
#             self.nume_prenume, self.ziua_de_nastere, self.__CNP = args
#         elif len(args) == 6:
#             (
#                 self.nume_prenume,
#                 self.ziua_de_nastere,
#                 self.numar_contact,
#                 self.oras,
#                 self.adresa,
#                 self.__CNP,
#             ) = args
#         else:
#             print("Numar invalid de argumente!")

#     # ===== Getter and Setter for CNP =====
#     def get_CNP(self):
#         return self.__CNP

#     def set_full_CNP(self, CNP):
#         self.__CNP = CNP

#     # ===== Method to display data =====
#     def afisare_date(self, index=None):
#         if index is not None:
#             print(f"\n----- Informatii persoana {index} -----")
#         else:
#             print("\n----- Informatii persoana -----")

#         print(f"Nume intreg: {self.nume_prenume}")
#         print(f"Ziua de nastere: {self.ziua_de_nastere}")
#         print(f"Numar de contact: {self.numar_contact}")
#         print(f"Oras: {self.oras}")
#         print(f"Adresa: {self.adresa}")
#         print(f"CNP: {self.__CNP}")


# # ===== Main program =====
# if __name__ == "__main__":
#     persoane = []

#     n = int(input("Cate persoane doriti sa introduceti? "))

#     for i in range(n):
#         print(f"\nIntroduceti datele pentru persoana {i + 1}:")
#         persoana = Human()
#         persoana.introducere_date()
#         persoane.append(persoana)

#     print("\n=== Lista de persoane introduse ===")
#     for i, persoana in enumerate(persoane, start=1):
#         persoana.afisare_date(index=i)


# class Human:
#     def __init__(
#         self,
#         nume_prenume: str = "",
#         ziua_de_nastere: str = "",
#         numar_contact: str = "",
#         oras: str = "",
#         adresa: str = "",
#         CNP: str = "",
#     ):
#         self.nume_prenume = nume_prenume
#         self.ziua_de_nastere = ziua_de_nastere
#         self.numar_contact = numar_contact
#         self.oras = oras
#         self.adresa = adresa
#         self.__CNP = CNP  # private attribute

#     # ===== Method 1: Introduce data manually =====
#     def introducere_date(self):
#         self.nume_prenume = input("Introduceti numele intreg (nume si prenume): ")
#         self.ziua_de_nastere = input("Introduceti ziua de nastere (ZZ-LL-AAAA): ")
#         self.numar_contact = input("Numar de telefon: ")
#         self.oras = input("Oras: ")
#         self.adresa = input("Adresa: ")
#         self.__CNP = input("Introduceti CNP din 12 cifre: ")

#     # ===== Method 2: Simulated method overloading =====
#     def set_date(self, *args):
#         """
#         Overloaded version of setting data.
#         1 argument → only nume_prenume
#         3 arguments → nume_prenume, ziua_de_nastere, CNP
#         6 arguments → all fields
#         """
#         if len(args) == 1:
#             self.nume_prenume = args[0]
#         elif len(args) == 3:
#             self.nume_prenume, self.ziua_de_nastere, self.__CNP = args
#         elif len(args) == 6:
#             (
#                 self.nume_prenume,
#                 self.ziua_de_nastere,
#                 self.numar_contact,
#                 self.oras,
#                 self.adresa,
#                 self.__CNP,
#             ) = args
#         else:
#             print("Numar invalid de argumente!")

#     # ===== Getter and Setter for CNP =====
#     def get_CNP(self):
#         return self.__CNP

#     def set_full_CNP(self, CNP):
#         self.__CNP = CNP

#     # ===== Method to display data =====
#     def afisare_date(self, index=None):
#         if index is not None:
#             print(f"\n----- Informatii persoana {index} -----")
#         else:
#             print("\n----- Informatii persoana -----")

#         print(f"Nume intreg: {self.nume_prenume}")
#         print(f"Ziua de nastere: {self.ziua_de_nastere}")
#         print(f"Numar de contact: {self.numar_contact}")
#         print(f"Oras: {self.oras}")
#         print(f"Adresa: {self.adresa}")
#         print(f"CNP: {self.__CNP}")


# # ===== Main program =====
# if __name__ == "__main__":
#     persoane = []

#     n = int(input("Cate persoane doriti sa introduceti? "))

#     for i in range(n):
#         print(f"\nIntroduceti datele pentru persoana {i + 1}:")
#         persoana = Human()
#         persoana.introducere_date()
#         persoane.append(persoana)

#     print("\n=== Lista de persoane introduse ===")
#     for i, persoana in enumerate(persoane, start=1):
#         persoana.afisare_date(index=i)


# Task 2
# Supplement the City class with a constructor,
# as well as the required overloaded methods.

# Task 3
# Supplement the Country class with a constructor,
# as well as the required overloaded methods.

# Task 4
# Supplement the Fraction class with a constructor,
# as well as the required overloaded methods.

# Task 5
# Implement a class Clock. Store the following in it:
# power type, manufacturer, year of manufacture, price,
# type (digital, tabletop, wall, regulator, etc.)
# Implement a constructor and class methods to input
# and output data, as well as other operations.
# Use method overloading.

# Task 6
# Implement a class Website. Store the following in it:
# website name, address, description. Implement a constructor
# and class methods to input and output data, as well as other
# operations. Use method overloading.


# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         """Overload the + operator"""
#         return Vector(self.x + other.x, self.y + other.y)

#     def __str__(self):
#         """Overload how the object prints"""
#         return f"({self.x}, {self.y})"


# v1 = Vector(1, 2)
# v2 = Vector(3, 4)
# v3 = v1 + v2  # Calls __add__
# print(v3)  # Calls __str__, outputs: (4, 6)


class City:
    def __init__(
        self,
        city_name="",
        region_name="",
        country_name="",
        number_of_citizens=0,
        zip_code="",
        area_code="",
    ):
        self.city = city_name
        self.region = region_name
        self.country = country_name
        self.number_of_citizens = number_of_citizens
        self.zip = zip_code
        self.code = area_code

    # “Overloaded” method: can get data from user OR from given values
    def input_data(
        self,
        city_name=None,
        region_name=None,
        country_name=None,
        number_of_citizens=None,
        zip_code=None,
        area_code=None,
    ):
        if city_name is not None:  # if values are given, use them
            self.city = city_name
            self.region = region_name
            self.country = country_name
            self.number_of_citizens = number_of_citizens
            self.zip = zip_code
            self.code = area_code
        else:  # otherwise ask the user to type info
            self.city = input("City name: ")
            self.region = input("Region name: ")
            self.country = input("Country name: ")
            self.number_of_citizens = input("Number of citizens: ")
            self.zip = input("ZIP code: ")
            self.code = input("Area code: ")

    # “Overloaded” display: full or short info
    def display(self, detailed=True):
        if detailed:
            print(f"City: {self.city}")
            print(f"Region: {self.region}")
            print(f"Country: {self.country}")
            print(f"Number of citizens: {self.number_of_citizens}")
            print(f"ZIP code: {self.zip}")
            print(f"Area code: {self.code}")
        else:
            print(f"{self.city}, {self.country}")


# Using constructor directly
# c1 = City("Paris", "Île-de-France", "France", 2148000, "75000", "+33")
# c1.display()        # shows all details
# c1.display(False)   # shows short info

# # Using input_data with arguments
# c2 = City()
# c2.input_data("London", "England", "UK", 8900000, "E1", "+44")
# c2.display()

# # Using input_data interactively (asks user for input)
# c3 = City()
# c3.input_data()
# c3.display()
