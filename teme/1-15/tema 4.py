# task 1
# # The user types in three numbers. The program prints the sum or product of these numbers based on the user's choice.

# number1 = int(input("Enter the first number:"))
# number2 = int(input("Enter the second number:"))

# print("Please select the operation you want to do with the values:\n1.Sum\n2.Product:")
# choice = int(input("Select (1-2):"))
# print(
#     "the numbers you choosed:", "\nfirst number:", number1, "\nsecond number:", number2
# )
# if choice == 1:
#     result = number1 + number2
#     print("the sum of the numbers is:", f"{number1}+{number2}" "=", result)
# elif choice == 2:
#     result = number1 * number2
#     print("the product of the numbers is:", f"{number1}*{number2}" "=", result)
# else:
#     print("No result")


# task 2
# The user types in three numbers. Based on the user's choice, the program prints a maximum of three, a minimum of three, or arithmetic mean of three numbers.

# num1 = int(input("enter 1-st number:"))
# num2 = int(input("enter 2-nd number:"))
# num3 = int(input("enter 3-rd number:"))
# print(
#     "Choose\n1.for the maximum number\n2.for the minimum number.\n3.for arithmetic mean of numbers"
# )
# choice = int(input("Select the number(1-3):"))
# if choice == 1:
#     result = max(num1, num2, num3)
#     print("the maximum number is:", result)
# elif choice == 2:
#     result = min(num1, num2, num3)
#     print("the minimum number is:", result)
# elif choice == 3:
#     result = num1 + num2 + num3
#     print("the sum of the numbers is:", result)
# else:
#     print("Invalid number!")


# Task 3
# The user types in the number of meters. Based on the user's choice, the program converts meters to miles, inches, or yards.

# Nota!
# Pentru a face putin  mai interactiva exercitiul mi-am folosit putin imaginatia "cum ar fi daca:"
#        si am facut putin research si am descoperit niste structuri utile.
# try - except ValueError - si apoi o structura secundara : while True cu continue, break sau exit.
# inca le analizez, dar intr-o oarecare masura le-am inteles putin :
# - creare bucle (loops) - structura try si except
# - sa ignore eroarea creata prin datele introduse prin consola si sa imi afiseze in schimb un mesaj scris prin linia de cod
# Ajutor am avut si din partea CHAT GPT si niste analiza.Voi reveni desigur asupra lor.

try:
    num1 = float(input("Enter meters:"))
    while True:
        print(
            "Choose convertor:\n1.Convert in miles:\n2.Convert in inches:\n3.Convert in yards.\n4.Exit"
        )
        choice = int(input("Select option:"))

        if choice == 1:
            rezultat = num1 / 1609.344
            print(rezultat, "miles")
        elif choice == 2:
            rezultat = num1 * 39.37
            print(rezultat, "inches")
        elif choice == 3:
            rezultat = num1 * 1.09361
            print(rezultat, "yards")
        elif choice == 4:
            print("Goodbye:")
            exit()
        else:
            print("please select a corect number from 1 to 4")
            continue

        while True:
            again = input("\n Do you want to return to the menu?(y/n):").strip().lower()
            if again == "y":
                break
            elif again == "n":
                print("See you!")
                exit()
            elif again == "exit":
                print("bye man!!!")
                exit()
            else:
                print("Invalid input, Please type'y' or 'exit' for yes or 'n' for no")
except ValueError:
    print("Invalid input. Please enter a number from 1 to 3")
