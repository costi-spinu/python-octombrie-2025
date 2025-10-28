# print("test print")

import math

import random

# print(random.random())
# print(random.randint(1, 11))
# # print(random.choices(1, 11))
# print(random.random() * 10)

# listaNumereExtragere = [1, 3, 5, 10, 123, 23]
# print(random.choice(listaNumereExtragere))


counter = 0


def functieTest(a, b):
    print("def function")
    counter = counter + 1
    # TODO: bug de rezolvat!
    if counter == 3:
        return
    functieTest(1, 2)


functieTest(1, 2)


# def sumaDouaNumere(a: int, b: int):
#     print("test")
#     print("1,2")
#     a + b + 3
#     return a + b


# print(sumaDouaNumere(1, 2))
# print(sumaDouaNumere(3, 200))


# def functie1():
#     print("test")


# functie1()
