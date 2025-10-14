# Task 3
# Write a function that prints an empty or solid square
# made out of some symbol. The function takes the following
# as parameters: the length of the side of the square, a symbol,
#  and a boolean variable:
# if it is True, the square is solid;
# if False, the square is empty.

print("Task 3")

import string
import random

num = random.randint(1, 10)
symbol = "".join(random.sample(string.punctuation, 1))
# num=int(input"Da-mi lungime:")
# symbol=(input"Da-mi simbol:")
print("Simbolul este:", symbol)
print("Lungimea este:", num)


def square(num: int, symbol: str, solid: bool):
    if solid:
        for c in range(num):
            print(num * symbol)
    else:
        print(symbol * num)
        for d in range(num - 2):
            print(symbol + " " * (num - 2) + symbol)
        if num > 1:
            print(symbol * num)


# square(5,"%",False)
square(num, symbol, False)
square(num, symbol, True)
