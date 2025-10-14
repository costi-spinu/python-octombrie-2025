# Task 1
# Write a program that requests two integers x and y, and then calculates and prints the value of x raised to the power of y.

try:
    while True:
        x = int(input("Please enter the value for X:"))
        y = int(input("Please enter the value for y:"))
        choice = int(
            input(
                f"Please choose which  operation you want to do with {x} and {y}\n\t 1. Sum\n\t 2. X raised to the power of y \n\t 3. Exit:\n",
            )
        )
        if choice == 1:
            suma = x + y
            print(f"The sum of {x} + {y} is:", suma)
        elif choice == 2:
            power = x**y
            print(f"The value of {x} raised to the power of {y} is:", power)
        elif choice == 3:
            print("Goodbye!")
            exit()
except ValueError:
    print("Invalit number")



