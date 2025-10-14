# Task 1
# Write a function that prints formatted text given below:
# "Don't compare yourself with anyone in this world...
#  if you do so, you are insulting yourself."
#                                           Bill Gates

print("Task 1")


# def printText():
#     print(
#         '"Don\'t compare yourself with anyone in this world....\n if you do so, you are insulting yourself.\n\t\t\t\t\tBill Gates"'
#     )


# printText()

# Task 2
# Write a function that takes two numbers as a parameter
#  and displays all even numbers in between.

print("Task 2")
# import random

# n1 = random.randint(1, 10)
# n2 = random.randint(1, 10)


# def evenNumbers(n1, n2):
#     c = min(n1, n2)
#     d = max(n1, n2)
#     print(f"Even numbers between {c} and {d} are:")
#     for a in range(c, d + 1):
#         c = []
#         if a % 2 == 0:
#             c.append(a)
#             print(c, end=" ")


# evenNumbers(n1, n2)


# Task 3
# Write a function that prints an empty or solid square
# made out of some symbol. The function takes the following
# as parameters: the length of the side of the square, a symbol,
#  and a boolean variable:
# if it is True, the square is solid;
# if False, the square is empty.

print("Task 3")

# import string
# import random

# num = random.randint(1, 10)
# symbol = "".join(random.sample(string.punctuation, 1))
# # num=int(input"Da-mi lungime:")
# # symbol=(input"Da-mi simbol:")
# print("Simbolul este:", symbol)
# print("Lungimea este:", num)


# def square(num: int, symbol: str, solid: bool):
#     if solid:
#         for c in range(num):
#             print(num * symbol)
#     else:
#         print(symbol * num)
#         for d in range(num - 2):
#             print(symbol + " " * (num - 2) + symbol)
#         if num > 1:
#             print(symbol * num)


# # square(5,"%",False)
# square(num, symbol, False)
# square(num, symbol, True)


# Task 4
# Write a function that returns the smallest of five numbers.
#  Numbers are passed as parameters.
print("Task 4")

# n1 = int(input("1st number:"))
# n2 = int(input("2nd number:"))
# n3 = int(input("3rd number:"))
# n4 = int(input("4th number:"))
# n5 = int(input("5th number:"))


# def smallestNumber(n1: int, n2: int, n3: int, n4: int, n5: int):
#     low = min(n1, n2, n3, n4, n5)
#     print(f"The smallest numbers from {n1},{n2},{n3},{n4} and {n5} is:", low)


# smallestNumber(n1, n2, n3, n4, n5)

# Task 5
# Write a function that returns the product of numbers in a
#  specified range. The start and end points of the range
# are passed as parameters. If the order of these points is
# incorrect (e.g., 5 is the end, and 25 is the start), swap them.

print("Task 5")

# import random
# import math
# n1=random.randint(1,100)
# n2=random.randint(1,100)

# def SumNumbers(n1:int,n2:int):
#     high=max(n1,n2)
#     low=min(n1,n2)
#     c=sum(range(low, high+1))
#     print (f"Suma din range-ul numerelor {low} si {high} este:",c)

# def ProductNumbers(n1:int,n2:int):
#     high=max(n1,n2)
#     low=min(n1,n2)
#     product=1
#     for d in range(low, high+1):
#             product*=d
#     print (f"Inmultirea dintre numerele din range-ul ({low}, {high} este:",product)
#     return product

# SumNumbers(n1,n2)
# ProductNumbers(n1,n2)

# Task 6
# Write a function that counts how many digits a number has.
# The number is passed as a parameter. Return the received
# number of digits from the function. For example, if the
# passed number is 3456, it has 4 digits.
print("Task 6")

# import random
# import string

# n = random.randint(1, 10)
# nn = "".join(random.sample((string.digits), n))
# num= random.randint(-10, 100)
# def nDigits(nn:string):
#     print ("The random number is:",nn)
#     return print (f"The number {nn} has ",len(nn),"digit(s)")
#     # varianta string

# def n2Digits(num:int):
#     print ("The random number is:",num)
#     return print (f"the number {num} has:",len(str(abs(num))),"digit(s).")
#     # varianta integer

# nDigits(nn)
# n2Digits(num)

# Task 7
# Write a function that checks if a number is a palindrome.
# The number is passed as a parameter. If the number is a palindrome,
# return true, otherwise false.

# A palindrome is a number which reads the same backward as forward.
#  For instance, 123321 is a palindrome, 546645 is a palindrome,
#  but 421987 is not.

print("Task 7")

# import random
# import string

# # num1=random.randint(1,100000) # verificare random
# # num1="".join(random.sample((string.digits),6)) # verificare string

# # num1 = 123321 #verificare
# # num1 = 421987 #verificare
# num1 = int(input("Introdu numar:"))


# def pNum(num1: int) -> bool:
#     a = str(num1)
#     if a == a[::-1]:
#         print(f'The number "{num1}" is palindrome')
#     else:
#         print(f'The number "{num1}" is not palindrome')


# pNum(num1)


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
