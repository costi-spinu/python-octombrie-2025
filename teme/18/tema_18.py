import math
import random

lung1 = random.randint(2, 20)
lung2 = random.randint(2, 20)
num1 = [random.randint(-100, 100) for c in range(lung1 + 1)]
num2 = [random.randint(-100, 100) for c in range(lung2 + 1)]
print(num1)


# Task 1
# Write a function that calculates the product of the elements from a list of integers.
#  The list is passed as a parameter. The result is returned from the function.
print("\tTask 1 Sum of integers")


def sum_elements(a):
    return sum(a)


print(f"Suma elementelor din {num1} este", sum_elements(num1))

# Task 2
# Write a function to find the minimum in a list of integers.
# The list is passed as a parameter. The result is returned from the function.

print("\tTask 2 Minimum integer")


def min_elements(a):
    return min(a)


print(f"Numarul cel mai mic din {num1} este", min_elements(num1))

# Task 3
# Write a function that determines how many prime numbers there are in the
# list of integers. The list is passed as a parameter. The result is returned
# from the function.
print("\tTask 3 Prime numbers")


def count_primes(numbers):
    count = 0
    for n in numbers:
        n = abs(n)  # make sure it's positive
        if n > 1:
            for i in range(2, n):
                if n % i == 0:
                    break
            else:
                count += 1
    return count


print(f"In lista {num1} sunt: {count_primes(num1)} numere prime")


# Task 4
# Write a function that removes a given number from the list of integers.
# Return the number of removed elements from the function.
print("\tTask 4 remove number")


def remove_number(num, lst):
    if num in lst:
        lst[:] = [x for x in lst if x != num]
        print(lst)


remove_number(num=int(input("da-mi nr:")), lst=num1)


# Task 5
# Write a function that takes two lists as a parameter and returns a
# list containing the elements of both lists.

print("\tTask 5 united lists")


def un_list(a, b):
    return a + b


print(f"Concatenarea celor doua liste", un_list(num1, num2))

# Task 6
# Write a function that calculates the power of each element from the
# list of integers. A value for the power is passed as a parameter,
# the list is also passed as a parameter. The function returns a new list
# containing the results.

print("\tTask 6 Raised to power")

num3 = random.randint(1, 10)


def power_integers(a, b):
    return [x**b for x in a]


print(
    f"Intreaga lista a fost ridicata la puterea {num3} iar rezultatul este:",
    power_integers(num1, num3),
)
