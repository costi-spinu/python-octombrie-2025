# Part 1

# Task 1

# Write a program that allows a user to calculate the quotient (division of one number by another) of two numbers.
#  The program accepts two values from the keyboard and returns the result of the operation to the screen.
#  Handle the exception that occurs during division by zero and print the error message.

# try:

#     a = float(input("enter a number: "))
#     b = float(input("enter second number: "))
#     c = a / b
#     print(c)

# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")

# except ValueError:
#     print("Error: you didn't enter a number")

# Task 2

# Implement the first task through a function.
#  The function must accept two parameters and display the result of division on the screen.
#  Create two versions of the function implementation:

# The first version does not handle the exception inside the function. All handling is on the outside;

# The second version handles the exception inside the function.


# def divide(a, b):
#     return a / b


# try:
#     a = float(input("enter a number: "))
#     b = float(input("enter second number: "))

#     c = divide(a, b)
#     print(c)

# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")

# except ValueError:
#     print("Error: you didn't enter a number")


# def divide2(a, b):
#     try:
#         c = a / b
#         print(c)
#     except ZeroDivisionError:
#         print("Error: Division by zero is not allowed.")

#     except ValueError:
#         print("Error: you didn't enter a number")


# a = input("enter a number: ")
# b = input("enter second number: ")
# divide2(a, b)

# Task 3

# Write a program that accepts a string and tries to convert it to a number.

# Handle the exception that occurs when the conversion fails, and print an error message.

# Task 4

# Implement the third task through a function.
#  The function should accept a string and display the result of the conversion on the screen.
#  Create two versions of the function implementation:

# The first version does not handle the exception inside the function. All handling is on the outside;

# The second version handles the exception inside the function.
######################################################################################################################
######################################################################################################################


# # # sayHiAdvanced = simpleDecorator(sayHi)
# # # print("Print intre functii")
# # # sayHiAdvanced()


# # @simpleDecorator_v2
# # @simpleDecorator
# # def sayHi():
# #     print("Welcome!")


# # sayHi()


# def simpleDecorator_v4(myFunction):
#     print("Hello! I'm Fourth Decorator!")

#     def simpleWrapper(argX, argY):
#         print("I've got {}, {}. Function starts working...".format(argX, argY))
#         resutl = myFunction(argX, argY)
#         print("See you!")
#         return resutl

#     return simpleWrapper


# @simpleDecorator_v4
# def calculateSum_v1(a, b):
#     print("Welcome! Let's calculate...")
#     x = int(input("x: "))
#     y = int(input("y: "))
#     return x + y + a + b


# print(calculateSum_v1(3, 4))

# # calculateSum_v1 = simpleDecorator_v4(calculateSum_v1)
# # print(calculateSum_v1(3, 4))


# Exceptions

# print(1 / 0)

# try:
#     amount = int(input("Enter the amount of received items: "))
#     items_type = input("Specify the type of received items: ")
#     parts_number = int(input("Enter the number of parts: "))
#     parts_amount = amount / parts_number
# except ValueError:
#     print("We need an integer for amount!")
# except ZeroDivisionError:
#     print("You cannot divide the delivery into 0 parts")


try:
    f = open("test.txt", "w")
    # perform file operations
finally:
    f.close()
