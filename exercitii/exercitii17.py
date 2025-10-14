# Task 1
# You have a set containing country names.
# Provide the following features:
# Add a country;
# Delete a country;
# Search for a country by entered characters;
# Check whether the country exists inside the set.

# country = {"Australia", "America", "Anglia", "America"}
# print(country)
# country.add("Venezuela")
# print(*country)
# country.remove("Australia")
# print(*country)
# s = input("da mi tara pe care vrei sa o cauti: ")
# if s in country:
#     print(True)
# else:
#     print(False)


# Task 2
# You have two sets containing city names.
# Create a third set containing names present in both sets.

# city1={"Alabama","Bucuresti","Damasc","Kiev"}
# city2={"Washington", "Ney York"}
# city3=city1|city2 #- UNION
# # print(city1&city2)  # - Intersection

# Task 3
# You have two sets containing city names.
# Create a third set containing names present
# in the first set but not in the second.
# city1 = {"Alabama", "Bucuresti", "Damasc", "Kiev"}
# city2 = {"Washington", "Ney York", "Kiev"}
# city3 = city1 - city2  # - difference
# print(city3)

# # Task 4
# # You have two sets containing city names.
# # Create a third set containing names present
# #  in the second set but not in the first.
# city1 = {"Alabama", "Bucuresti", "Damasc", "Kiev"}
# city2 = {"Washington", "Ney York", "Kiev"}
# city3 = city2 - city1  # - difference
# print(city3)


# # Task 5
# # You have two sets containing city names.
# # Create a third set containing names unique to each set.
# city = {"Alabama", "Bucuresti", "Damasc", "Kiev", "Oslo"}
# cities = {"washington", "New York", "Kiev"}
# citix2 = cities - city
# citix3 = city - cities
# print(citix2 | citix3)

# Task 6
# A dictionary contains a set of pairs:
# Country name -> Capital. Provide the possibility
# to add, delete, search, and replace them.

# d = dict({("Austria", "Viena"), ("USA", "Washington D.C"), ("USA", "Washington D.C")})
# print(d)
# print(type(d))
# t = dict({("Romania", "Bucuresti")})
# print(t)
# d.update(t)  # add
# print(d)
