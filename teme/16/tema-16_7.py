# Task 7
# Write a function that checks if a number is a palindrome.
# The number is passed as a parameter. If the number is a palindrome,
# return true, otherwise false.

# A palindrome is a number which reads the same backward as forward.
#  For instance, 123321 is a palindrome, 546645 is a palindrome,
#  but 421987 is not.

print("Task 7")

import random
import string

# num1=random.randint(1,100000) # verificare random
# num1="".join(random.sample((string.digits),6)) # verificare string

# num1 = 123321 #verificare
# num1 = 421987 #verificare
num1 = int(input("Introdu numar:"))


def pNum(num1: int) -> bool:
    a = str(num1)
    if a == a[::-1]:
        print(f'The number "{num1}" is palindrome')
    else:
        print(f'The number "{num1}" is not palindrome')


pNum(num1)
