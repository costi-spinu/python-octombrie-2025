# try:
#     # Introducerea numerelor o singură dată
#     num1 = int(input("Enter 1st number: "))
#     num2 = int(input("Enter 2nd number: "))
#     num3 = int(input("Enter 3rd number: "))

#     while True:
#         print(
#             "\nChoose:"
#             "\n1. Maximum number"
#             "\n2. Minimum number"
#             "\n3. Sum of numbers"
#             "\n4. Exit"
#         )

#         choice = int(input("Select an option (1-4): "))

#         if choice == 1:
#             result = max(num1, num2, num3)
#             print("The maximum number is:", result)
#         elif choice == 2:
#             result = min(num1, num2, num3)
#             print("The minimum number is:", result)
#         elif choice == 3:
#             result = num1 + num2 + num3
#             print("The sum of the numbers is:", result)
#         elif choice == 4:
#             print("Goodbye!")
#             break
#         else:
#             print("Invalid option. Please choose between 1 and 4.")

#         # Întrebăm dacă vrea să revină la meniu
#         again = input("\nDo you want to go back to the menu? (y/n): ").strip().lower()
#         if again != "y":
#             print("Goodbye!")
#             break

# except ValueError:
#     print("Invalid input. Please enter only numbers.")


# try:
#     x = int(input("Introdu un număr: "))
#     print("Numărul introdus este:", x)
# except ValueError:
#     print("Nu ai introdus un număr valid!")


try:
    num1 = int(input("enter 1-st number:"))
    num2 = int(input("enter 2-nd number:"))
    num3 = int(input("enter 3-rd number:"))
    while True:
        print(
            "Choose\n1.for the maximum number\n2.for the minimum number.\n3.for arithmetic mean of numbers"
        )
        choice = int(input("Select the number(1-3):"))
        if choice == 1:
            result = max(num1, num2, num3)
            print("the maximum number is:", result)
        elif choice == 2:
            result = min(num1, num2, num3)
            print("the minimum number is:", result)
        elif choice == 3:
            result = num1 + num2 + num3
            print("the sum of the numbers is:", result)
        else:
            print("Invalid number! Please enter a valid number")
            continue
        while True:
            again = input("\n Do you want to return to the menu?(y/n):").strip().lower()
            if again == "y":
                break
            elif again == "n":
                print("Bye bye!")
                exit()
            else:
                print("Invalid input, Please type'y' for yes or 'n' for no")
except ValueError:
    print("Invalid input. Please enter a number:")
