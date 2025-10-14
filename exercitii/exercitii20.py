# Task 1
# Create a function that returns all even numbers in a range.
# The function takes the beginning and the end of the range
# as parameters. Use the generator mechanism within the function.


def evenNumbers(start:int, end:int):
    low = min(start, end)
    high = max(start, end)
    for i in range(low, high + 1):
        if i % 2 == 0:
            yield i


import random

n = random.randint(1, 100)
x = random.randint(-100, 100)
numbers = [random.randint(1, 100) for c in range(n)]

for num in evenNumbers(n, x):
    print(num,end=" ")


# Task 2
# Create a function that returns all values from a list that
#  are in a range specified by a user. The function takes the
# list, the beginning and the end of the range as parameters.
# Use the generator mechanism within the function.


# def values_range(a, c, d):
#     low = min(c, d)
#     high = max(c, d)
#     for v in a:
#         if low < v < high:
#             yield v


# for valoare in values_range(numbers, n, x):
#     print(valoare, end=" ")


# # Task 3
# # To solve this task, be sure to use the mechanism of higher
# # order functions. Create a function that checks the passed
# # number to be even or odd. A user determines what to check
# # for (evenness or oddness).

# # The function signature is:
# # def check_value(value_to_check, function_to_call)
# # value_to_check — a value to check.
# # function_to_call — a function to check (function to check
# # evenness or function to check oddness).


# def even_1(a):
#     return a % 2 == 0


# def odd_1(a):
#     return a % 2 != 0


# def check(func, num):
#     return func(num)


# num = int(input("Da-mi nr: "))
# choice = input("Alegeti optiune:\n1. Verificare numar par\n2. Verificare numar impar\n")

# if choice == "1":
#     if check(even_1, num):
#         print("Numarul este par.")
#     else:
#         print("Numarul NU este par.")
# elif choice == "2":
#     if check(odd_1, num):
#         print("Numarul este impar.")
#     else:
#         print("Numarul NU este impar.")
# else:
#     print("Optiune invalida!")


# # Task 4
# # Create a function to display the current time. The function
# # takes no parameters. Without using decorator syntax, decorate
# # the function with another function. Potential data output to
# # the screen:
# # ***************************
# # 23:00
# # ***************************
# # In this output, the two lines of asterisks are the result
# # of decorating.

# import datetime


# # decoratorul
# def star_decorator(func):
#     def wrapper():
#         print("*" * 27)
#         func()
#         print("*" * 27)

#     return wrapper


# # funcția de bază
# def show_time():
#     now = datetime.datetime.now()
#     print(now.strftime("%H:%M"))


# # decorare manuală (fără @)
# decorated_show_time = star_decorator(show_time)

# # apel
# decorated_show_time()

# # Task 5
# # Add to the task 4 another function to decorate the data output.
# # This function should add new elements to the formatting of the output.

# import datetime


# # Primul decorator: linii cu asteriscuri
# def star_decorator(func):
#     def wrapper():
#         print("*" * 27)
#         func()
#         print("*" * 27)

#     return wrapper


# # Al doilea decorator: mesaj suplimentar
# def message_decorator(func):
#     def wrapper():
#         print(">>> Current Time:")
#         func()

#     return wrapper


# # Funcția de bază
# def show_time():
#     now = datetime.datetime.now()
#     print(now.strftime("%H:%M"))


# # Aplicare manuală a decoratoarelor
# decorated_show_time = star_decorator(message_decorator(show_time))

# # Apel
# decorated_show_time()

# # Task 6
# # Do the task 4 using the decorator syntax.

# import datetime


# # Decorator: adaugă linii cu asteriscuri
# def star_decorator(func):
#     def wrapper():
#         print("*" * 27)
#         func()
#         print("*" * 27)

#     return wrapper


# # Funcția de bază decorată cu sintaxa @
# @star_decorator
# def show_time():
#     now = datetime.datetime.now()
#     print(now.strftime("%H:%M"))


# # Apel
# show_time()
