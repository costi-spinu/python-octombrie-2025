# Task 3
# Write a program that allows a user to enter a set
#  of positive (numbers greater than zero) numbers
# from the keyboard. The numbers should be accumulated
# in a list. After receiving all the values, the program
# should analyze the data. If a negative value is detected,
# the program should generate an exception. If all values
# in the list are positive, the program should return to
# the screen the sum of all the numbers in the list.
# The exception generated should be handled by the program code.


def introduce_numere():
    numere = []
    print("Introduce numere pozitive si scrie 'gata' cand ai terminat:")

    while True:
        val = input("Numar: ")
        if val.lower() == "gata":
            break
        try:
            num = int(val)
            if num <= 0:
                print("Te rog introduce doar numere pozitive!")
            else:
                numere.append(num)
        except ValueError:
            print("Te rog introduce doar valori numerice!")

    if numere:
        print(f"Lista numerelor introduse: {numere}")
        print(f"Suma numerelor introduse este: {sum(numere)}")
    else:
        print("Nu exista numere introduse")


introduce_numere()
