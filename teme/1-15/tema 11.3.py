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
