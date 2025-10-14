# Task 6
# Write a function that counts how many digits a number has.
# The number is passed as a parameter. Return the received
# number of digits from the function. For example, if the
# passed number is 3456, it has 4 digits.
print("Task 6")

import random
import string

n = random.randint(1, 10)
nn = "".join(random.sample((string.digits), n))
num = random.randint(-10, 100)


def nDigits(nn: string):
    print("The random number is:", nn)
    return print(f"The number {nn} has ", len(nn), "digit(s)")
    # varianta string


def n2Digits(num: int):
    print("The random number is:", num)
    return print(f"the number {num} has:", len(str(abs(num))), "digit(s).")
    # varianta integer


nDigits(nn)
n2Digits(num)
