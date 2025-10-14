# Task 5
# Write a function that returns the product of numbers in a
#  specified range. The start and end points of the range
# are passed as parameters. If the order of these points is
# incorrect (e.g., 5 is the end, and 25 is the start), swap them.

print("Task 5")

import random
import math

n1 = random.randint(1, 100)
n2 = random.randint(1, 100)


def SumNumbers(n1: int, n2: int):
    high = max(n1, n2)
    low = min(n1, n2)
    c = sum(range(low, high + 1))
    print(f"Suma din range-ul numerelor {low} si {high} este:", c)


def ProductNumbers(n1: int, n2: int):
    high = max(n1, n2)
    low = min(n1, n2)
    product = 1
    for d in range(low, high + 1):
        product *= d
    print(f"Inmultirea dintre numerele din range-ul ({low}, {high} este:", product)
    return product


SumNumbers(n1, n2)
ProductNumbers(n1, n2)
