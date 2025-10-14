# Task 1

# The user types in a number of the month (from 1 to 12).
# Based on the typed in number, the program displays one of the following:
# Winter if the number is 1, 2, or 12, Spring if the number is in the range
# from 3 to 5, Summer if from 6 to 8, Autumn if from 9 to 11.
# If the number is out of the range, display an error message.

num = int(input("Enter a number from 1 to 12:"))

if num == 1 or num == 2 or num == 12:
    print("Winter")
elif num == 3 or num == 4 or num == 5:
    print("Spring")
elif num == 6 or num == 8:
    print("Sommer")
else:
    print("Autumn")


# Task 2

# The user types in a six-digit number. Write a program that determines
# if this number is lucky. (A lucky number is a six-digit number with
# the sum of its first three digits being equal to the sum of its last three digits.)

# For example, 123321 is a lucky number because 1+2+3 = 3+2+1.

# But 378423 is not a lucky number because 3+7+8 != 4+2+3.

# If the user typed in a non-six-digit number, display an error message.

# sixdigit = int(input("Introdu 6 numere:"))


def is_lucky_number(number_str):
    # Check if the input is exactly 6 digits and all characters are digits
    if len(number_str) != 6 or not number_str.isdigit():
        return "Error: Please enter a valid six-digit number."

    # Split the number into first and last three digits
    first_half = number_str[:3]
    second_half = number_str[3:]
    # Calculate the sums
    sum_first_half = sum(int(digit) for digit in first_half)
    sum_second_half = sum(int(digit) for digit in second_half)

    # Determine if it's lucky
    if sum_first_half == sum_second_half:
        return "Lucky number!"
    else:
        return "Not a lucky number."


# Get user input
user_input = input("Enter a six-digit number: ")
result = is_lucky_number(user_input)
print(result)

# ------------------------------

a = int(input("da mi nr de 6 cifre"))
b = a // 100000 % 10
c = a // 10000 % 10
d = a // 1000 % 10
e = a // 100 % 10
f = a // 10 % 10
g = a % 10
if (b + c + d) == (e + f + g):
    print("a lucky number is ", a)
else:
    print(a, "is not a lucky number")


# ----------------------------------
numar = input("Introdu un numar de 6 cifre: ")

if len(numar) != 6:
    print("Trebuie sa introduci un numar de 6 cifre")
else:
    cifra1 = int(numar[0])
    cifra2 = int(numar[1])
    cifra3 = int(numar[2])
    cifra4 = int(numar[3])
    cifra5 = int(numar[4])
    cifra6 = int(numar[5])

    suma_la_stanga = cifra1 + cifra2 + cifra3
    suma_la_dreapta = cifra4 + cifra5 + cifra6

    if suma_la_stanga == suma_la_dreapta:
        print(f"Numarul {numar} este norocos")
    else:
        print(f"Numarul {numar} nu este norocos")
