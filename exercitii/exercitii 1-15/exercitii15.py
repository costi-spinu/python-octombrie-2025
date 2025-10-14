# # Task 1
# # The user inputs a fruit from the keyboard.
# #  Display the number of times this fruit occurs as an element.

# fruits = ["banana", "mar", "pere", "mango"]
# fruit = input("Write a fruit:").strip().lower()
# countfruit = fruits.count(fruit)
# print(countfruit)


# # Task 2
# # Improve Task 1 by adding the possibility to
# # calculate how many times this fruit occurs
# # as a part of an element. Here, for example,
# # "banana, apple, bananamango, mango, strawberry-banana".
# # The word "banana" occurs three times.

# fruits = ["banana", "apple", "bananamango", "mango", "strawberry-banana"]

# fruit_input = input("Enter a fruit: ")

# count = sum(element.count(fruit_input) for element in fruits)

# print(f"The word '{fruit_input}' occurs {count} times (including inside elements).")


# # Task 3
# # You have a tuple containing names of car manufacturers (a name may occur from 0 to N times).
# #  The user inputs a manufacturer and a replacement word. Replace all elements in
# # the tuple with the replacement word. The match must be complete.

# cars = ("Toyota", "BMW", "Audi", "BMW", "Mercedes", "BMW", "Ford")

# # User input
# target = input("Enter the manufacturer to replace: ").strip()
# replacement = input("Enter the replacement word: ").strip()

# # Replace occurrences (exact match only)
# updated_cars = tuple(replacement if car == target else car for car in cars)

# # Display result
# print("Original tuple:", cars)
# print("Updated tuple: ", updated_cars)


# Task 4
# You have a tuple of integers. Display statistics on the number of digits in tuple elements. For instance:
# One digit — 3 elements;
# Two digits — 4 elements;
# Three digits — 5 elements.

import random

lun = random.randint(5, 10)
lista = tuple(random.randint(1, 999) for c in range(lun))
print(lista)

l1 = 0
l2 = 0
l3 = 0
for i in lista:
    if i in range(1, 9):
        l1 += 1
    elif i in range(10, 99):
        l2 += 1
    elif i in range(100, 999):
        l3 += 1

print(f"o singura cifra: {l1}\n doua cifre: {l2}\n trei cifre: {l3}")
