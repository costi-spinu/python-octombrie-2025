# Task 1
# The user types in a number. Determine how many digits this number has,
# find their sum and average. Determine how many zeros this number has.
# Implement a dialog with the user through a menu.

num = input("Introduceți un număr: ")

# eliminăm semnul dacă e negativ
if num.startswith("-"):
    num = num[1:]

while True:
    print("\nMeniu:")
    print("1 - Numărul de cifre")
    print("2 - Suma cifrelor")
    print("3 - Media cifrelor")
    print("4 - Numărul de zerouri")
    print("5 - Ieșire")

    opt = input("Alegeți opțiunea: ")

    if opt == "1":
        print("Numărul de cifre:", len(num))
    elif opt == "2":
        print("Suma cifrelor:", sum(int(c) for c in num))
    elif opt == "3":
        print("Media cifrelor:", sum(int(c) for c in num) / len(num))
    elif opt == "4":
        print("Numărul de zerouri:", num.count("0"))
    elif opt == "5":
        break
    else:
        print("Opțiune invalidă!")


# Task 2
# Write a program that displays a chessboard with a set cell size. For example, three,
# ***---***---***---***---
# ***---***---***---***---
# ***---***---***---***---
# ---***---***---***---***
# ---***---***---***---***
# ---***---***---***---***


cell = 3  # dimensiunea unei celule
size = 6  # numărul de celule pe o linie

for r in range(size):
    for _ in range(cell):
        for c in range(size):
            print(("***" if (r + c) % 2 == 0 else "---"), end="")
        print()

# Task 3
# Write a program that tests users for their multiplication table skills.
# The program prints two numbers, and the user must enter their product.
# Develop several levels of difficulty (they should differ in complexity and number of questions).
# Print the points that represent the user's skills.

import random

nivel = int(input("Nivel (1-usor, 2-mediu, 3-greu): "))
if nivel == 1:
    max_num, intrebari = 5, 5
elif nivel == 2:
    max_num, intrebari = 10, 7
else:
    max_num, intrebari = 20, 10

scor = 0
for i in range(intrebari):
    a = random.randint(1, max_num)
    b = random.randint(1, max_num)
    if int(input(f"{a} x {b} = ")) == a * b:
        scor += 1

print(f"Scor: {scor}/{intrebari}")


# Task 4
# Print a rhombus made out of asterisks.

n = int(input("Enter size (n >= 1): "))

# top half (including middle row)
for i in range(n):
    print(" " * (n - 1 - i) + "*" * (2 * i + 1))

# bottom half
for i in range(n - 2, -1, -1):
    print(" " * (n - 1 - i) + "*" * (2 * i + 1))
