# Task 1
# Write a function that prints formatted text given below:
# "Don't compare yourself with anyone in this world...
#  if you do so, you are insulting yourself."
#                                           Bill Gates

print("Task 1")


def printText():
    print(
        '"Don\'t compare yourself with anyone in this world....\n if you do so, you are insulting yourself.\n\t\t\t\t\tBill Gates"'
    )


printText()

# Task 2
# Write a function that takes two numbers as a parameter
#  and displays all even numbers in between.

print("Task 2")
import random

n1 = random.randint(1, 10)
n2 = random.randint(1, 10)


def evenNumbers(n1, n2):
    c = min(n1, n2)
    d = max(n1, n2)
    print(f"Even numbers between {c} and {d} are:")
    for a in range(c, d + 1):
        c = []
        if a % 2 == 0:
            c.append(a)
            print(c, end=" ")


evenNumbers(n1, n2)
