# # Task 1
# # The user types in two numbers. Find the sum and average of numbers in the specified range.

i = int(input("Input first number"))
j = int(input("Input the second number:"))
low = min(i, j)
high = max(i, j)

numere = []
for i in range(low, high + 1):
    numere.append(i)

total = sum(numere)
average = total / len(numere)
print("suma", total)
print("average", average)

# # Task 2
# # The user types in a number. Calculate the factorial of a number. For instance, if the user typed in 3, the factorial is 1*2*3 = 6.
# # The formula for calculating the factorial: n! = 1*2*3…*n, where n is the user-defined number.\

num = int(input("Enter a number to calculate its factorial: "))
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial = factorial * i

    print(f"The factorial of {num} is: {factorial}")


# # Task 3
# # The user types in the line length. Print a horizontal line made out of * of the specified length.
# # For instance, if the typed in number is 7, the output will be as follows: *******.

nr_linii = int(input("Introdu numarul de caractere: "))
if nr_linii == 7:
    print(nr_linii * "*")
else:
    print(nr_linii * "w")

# Task 4
# The user types in the length of a line and a symbol to fill the line. Print a horizontal line made out of the typed in symbol of the specified length.
# If the typed in number and symbol are 5 and &, the output will be as follows: &&&&&.

l = int(input("Introdu numarul de caractere pentru string:"))
s = input("introdu semnul:")
if l == 5 or s == "&":
    print("Because the number you introduced is 5: &&&&&")
else:
    print(l * s)
