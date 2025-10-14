# Module: Exceptions
# Part 1
# Task 1
# Write a program that asks a user for name and age.
# After receiving the data, the program must output a
#  greeting in the format: "Hello, {name}! Your age is
#  {age}". Handle an exception that occurs when an
# invalid age is entered (age < 0 or age > 130) and
#  output an error message.

try:
    print("Hello")
    print("My name in Compo, please input your name and age\n")
    name = input("name:")
    age = int(input("age:"))
    if age < 0 or age > 130:
        raise ValueError("Age must be between 0 and 130")

    print(f"Hello {name}! Your age is {age}.")
except ValueError:
    print("Invalid age is entered")
