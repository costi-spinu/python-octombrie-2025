# Task 1

# Write a function that calculates the sum of elements from a list of
# integers. The list is passed as a parameter.

import math
import random

lung = random.randint(2, 2)
lung2 = random.randint(1, 10)
numbers = [random.randint(1, 100) for c in range(lung)]
numbers2 = [random.randint(-100, 100) for c in range(lung2)]


def sumElements(d):
    return sum(d)


print("Task1:\n\t", f"suma numerelor {numbers} este", sumElements(numbers))


# Task 2

# Write a function to find the maximum in the list of integers.
# The list is passed as a parameter.


def maximInteger(e):
    return max(e)


print("Task2:\n\t", f"numarul maxim din lista {numbers2} este", maximInteger(numbers2))


# Task 3

# Write a function that determines the number of even, odd, positive,
#  negative elements in the list of integers. The list is passed as a parameter.


def evenOddPositive(g):
    even = []
    odd = []
    positive = []
    negative = []
    print("Task3:\n\t" + "Lista:", g)

    for num in g:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

        if num >= 0:
            positive.append(num)
        else:
            negative.append(num)

    print("\tNumere pare sunt:", even)
    print("\tNumerele impare sunt:", odd)
    print("\tNumerele pozitive sunt:", positive)
    print("\tNumerele negative sunt:", negative)


evenOddPositive(numbers2)

# Task 4

# Write a function that flips the contents of the list of integers.


def flip_list(lst):
    return lst[::-1]


print("Task 4:\n\t" + "Lista inversata", flip_list(numbers2))

# # Task 5

# # Write a function that searches for some number in the list of integers.

print("Task 5:\n\t")


def searchList(num):
    if num in numbers2:
        return print("numarul se regaseste in lista")
    else:
        return print("numarul nu exista ")


searchList(num=int(input("numarul:")))

# Task 6

# Write a function that calculates the factorial of each element
# in the list of integers. The function returns a new list containing the
# resulting factorials.


def factorial_list(lst):
    result = []
    for num in lst:
        if num >= 0:
            result.append(math.factorial(num))
        else:
            result.append(None)  # factorial not defined for negative numbers
    return result


print("Task 6:\n\tLista factorialelor:", factorial_list(numbers2))
