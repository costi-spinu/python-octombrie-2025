# Task 1
# Write a program that asks a user for a number
# and calculates its factorial. Handle an exception
#  that occurs when a negative number is entered, and
# print an error message.


# Task 2
# Implement the first task through a function.
# The function should take a number as a parameter
# and return the factorial. The correctness check of
# the data obtained must be inside the function.
#  Create two versions of the function implementation:
# The first version does not handle the exception
#  inside the function. All handling is on the outside;
# The second version handles the exception inside the function.


import itertools
import math


def factorial_v1(n):
   
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_v1(n - 1)


def factorial_v2(n):
  
    try:
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial_v2(n - 1)
    except ValueError as e:
        print("Error:", e)
        return None


def permutari(nume):
    permutari = list(itertools.permutations(nume))
    print(f"\nAi introdus {len(nume)} persoane.")
    print(f"Numărul total de aranjamente posibile este: {math.factorial(len(nume))}\n")

    for i, p in enumerate(permutari, start=1):
        print(f"{i}. {', '.join(p)}")


try:
    while True:
        print("\nSelect choice")
        print("1. Factorial number (V1 - excepție afară)")
        print("2. Factorial number (V2 - excepție în funcție)")
        print("3. Factorial names (permutări)")
        print("4. Exit")
        choice = int(input("Choice (1-4): "))

        if choice == 1:  # V1
            try:
                num = int(input("Enter a number: "))
                if num < 0:
                    raise ValueError("Factorial is not defined for negative numbers.")
                print(f"[V1] Factorial of {num} is {factorial_v1(num)}")
            except ValueError as e:
                print("Error:", e)

        elif choice == 2:  # V2
            num = int(input("Enter a number: "))
            result = factorial_v2(num)
            if result is not None:
                print(f"[V2] Factorial of {num} is {result}")

        elif choice == 3:  # permutări
            nume = input("Introdu numele persoanelor separate prin spațiu: ").split()
            permutari(nume)

        elif choice == 4:
            print("La revedere!")
            break

        else:
            print("Alegere invalidă. Încearcă din nou.")

except ValueError as e:
    print("Error:", e)
