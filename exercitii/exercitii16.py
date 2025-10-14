# Task 1
# Write a function that prints formatted text given below:

# "Don't let the noise of others' opinions
# # drown out your own inner voice."Steve Jobs

print("Task1")
# def printtext():
#     print(
#     "\"Don't let the noise of others' opinions\ndrown out your own inner voice.\"Steve Jobs"
# )
# printtext()
# # Task 2
# # Write a function that takes two numbers as a
# # parameter and displays all odd numbers in between.

print("Task2")
# import random

# start = random.randint(1, 10)
# end = random.randint(1, 100)


# def display_odd_numbers(start, end: int):
#     if start > end:
#         start, end = end, start
#     for num in range(min(start, end) + 1, max(start, end)):
#         if num % 2 != 0:
#             print(num, end=" ")


# display_odd_numbers(start, end)

# n = int(input("da mi nr: "))


# def impar(a):
#     c = []
#     for i in range(a):
#         if i % 2 != 0:
#             c.append(i)
#     print(*c, sep=",")
#     return c


# f = impar(n)
# print(f)

# Task 3
# Write a function that prints a horizontal or
# vertical line made out of some symbol.
# The function takes the following as a parameter:
#  the line's length, direction, symbol.

print("Task3")
# a = int(input("da mi dimensiune"))
# b = input("da mi simbol:")
# c = input("directie (vertical/orizontal): ")


# def afisare1(a, b, c):
#     if c.lower() == "orizontal":
#         print(b * a)
#     elif c.lower() == "vertical":
#         for i in range(a):
#             print(b)

# afisare1(a, b, c)

# Task 4
# Write a function that returns the greatest of four numbers.
# Numbers are passed as parameters.

print("Task4")


# def numarmaxim():
#     while True:
#         a = int(input("introduce primul numar:"))
#         b = int(input("introduce al doilea numar:"))
#         c = int(input("introduce al treilea numar:"))
#         d = int(input("introduce al patrulea numar:"))
#         if a == " " or b == " " or c == " " or d == " ":
#             print("Please input only numbers")
#         else:
#             return print(max(a, b, c, d))


# numarmaxim()
###########################
# def maxi():
#     n1 = list(map(int, input().split(",")))
#     print(max(n1))


# maxi()


# Task 5
# Write a function that returns the sum of numbers in a
# specified range. The start and end points of the range
# are passed as parameters.

print("Task5")

# n1 = int(input("da mi limita inferioara: "))
# n2 = int(input("da mi limita superioara: "))


# def sum(a, b):
#     c = 0
#     d = min(a, b)
#     g = max(a, b)
#     for i in range(d, g):
#         c += i
#     return c


# s = sum(n1, n2)
# print(s)

# Task 6
# Write a function that checks if a number is prime.
# The number is passed as a parameter. If the number
#  is prime, return true, otherwise false.

print("Task6")
# n = int(input("da mi nr: "))


# def prim(a):
#     d = 0
#     if a < 2:
#         return False
#     else:
#         for i in range(2, a):
#             if a % i == 0:
#                 d += 1
#                 break
#         if d == 0:
#             return True
#         else:
#             return False


# t = prim(n)
# print(t)


# Task 7
# Write a function that checks if a six-digit number
# is lucky. The number is passed as a parameter.
# If the number is lucky, return true, otherwise false.
# A lucky six-digit number is a number with the sum
#  of its first three digits being equal to the sum
# of its last three digits. For example, 123420 is a
# lucky number because 1+2+3 = 4+2+0, and 723422 is not
# because 7+2+3 != 4+2+2.

print("Task7")
# import string
# import random

# n = random.sample(range(1, 9), 6)
# print(n)


# def lucky(n):
#     s = 0
#     s1 = 0
#     for i in range(len(n)):
#         if i < 3:
#             s += n[i]
#         else:
#             s1 += n[i]
#     if s == s1:
#         print("{} is lucky".format(n))
#     else:
#         print("{} is not lucky".format(n))


# lucky(n)
