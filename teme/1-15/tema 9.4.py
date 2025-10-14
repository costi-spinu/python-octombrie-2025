# Task 4
# The user types in an integer value. Remove all 3s and 6s from this integer and print it.

# varianta eliminare 3 si 6 din range
try:

    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    low = min(num1, num2)
    high = max(num1, num2)
    eliminated_numbers = []

    print("Filtred numbers are:")
    for c in range(low, high + 1):
        digits = str(c)
        filtru = "".join(d for d in digits if d not in ["3", "6"])
        if len(filtru) != 0:
            print(filtru)
        else:
            eliminated_numbers.append(c)
    print("The numbers which were complete eliminated are:")
    print(eliminated_numbers)


except ValueError:
    print("Invalid input!")


# varianta simpla
num = input("Enter an integer: ")
clean_num = "".join([digit for digit in num if digit not in "36"])
print(f"Number after removing all 3s and 6s: {clean_num}")
