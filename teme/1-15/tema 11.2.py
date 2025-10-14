# Task 2
# Write a program that displays a chessboard with a set cell size. For example, three,
# ***---***---***---***---
# ***---***---***---***---
# ***---***---***---***---
# ---***---***---***---***
# ---***---***---***---***
# ---***---***---***---***


num1 = int(input("Enter the width for chessboard:"))
num2 = int(input("Enter the lenght/height for chessboard:"))
for i in range(num2):
    c = num2 / 2
    if i < c:
        print((num1 * "*" + num1 * "-") * 4)
    else:
        print((num1 * "-" + num1 * "*") * 4)
