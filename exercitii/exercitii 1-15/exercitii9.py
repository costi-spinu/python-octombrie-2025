# # Task 1
# # Print the multiplication table for the user-defined number. If the user typed in 7, the output should be as follows:
# # 7 * 1 = 7
# # 7 * 2 = 14
# # 7 * 3 = 21


# # number = int(input("Enter a number: "))

# # for i in range(1, 11):
# #     print(f"{number} * {i} = {number * i}")


# # Task 2
# # Write a currency converter program. Implement a dialog with the user through a menu.


# def display_menu():
#     print("\nCurrency Converter Menu:")
#     print("1. Convert USD to EUR")
#     print("2. Convert EUR to USD")
#     print("3. Convert USD to GBP")
#     print("4. Convert GBP to USD")
#     print("5. Exit")


# def convert_currency(amount, rate):
#     return round(amount * rate, 2)


# def currency_converter():
#     # Example exchange rates (you can update these or make them dynamic)
#     usd_to_eur = 0.91
#     eur_to_usd = 1.10
#     usd_to_gbp = 0.78
#     gbp_to_usd = 1.28

#     while True:
#         display_menu()
#         choice = input("Enter your choice (1-5): ")

#         if choice == "5":
#             print("Exiting Currency Converter. Goodbye!")
#             break
#         elif choice in ["1", "2", "3", "4"]:
#             try:
#                 amount = float(input("Enter amount to convert: "))
#                 if amount < 0:
#                     print("Amount must be positive.")
#                     continue
#             except ValueError:
#                 print("Invalid amount. Please enter a number.")
#                 continue

#             if choice == "1":
#                 result = convert_currency(amount, usd_to_eur)
#                 print(f"${amount} USD = €{result} EUR")
#             elif choice == "2":
#                 result = convert_currency(amount, eur_to_usd)
#                 print(f"€{amount} EUR = ${result} USD")
#             elif choice == "3":
#                 result = convert_currency(amount, usd_to_gbp)
#                 print(f"${amount} USD = £{result} GBP")
#             elif choice == "4":
#                 result = convert_currency(amount, gbp_to_usd)
#                 print(f"£{amount} GBP = ${result} USD")
#         else:
#             print("Invalid option. Please choose a number between 1 and 5.")


# currency_converter()
# Task 3
# The user types in the start and end points of the range and a number. If the number is not in
# the range, the program asks the user to re-enter the number, and so on until the user enters the
# number correctly. The program displays all numbers in the range, highlighting the number with
# exclamation marks. For instance: 1 2 3 !4! 5 6 7.

try:
    for c in range(1, 11):
        while True:
            number = int(input("Enter number:"))
            print("For exit - 100")
            if number == 100:
                print("Bye")
                exit()
            elif number > c or number < c:
                print("Your number is out of range")
                break
            else:
                print("correct number!")
                break

except ValueError:
    print("Incorrect!")


# Task 4
# Develop a game Guess the Number. The program chooses a number in the range from 1 to 500.
# The user tries to guess it. After each try, the program gives hints on whether the number is
# greater or less than the guessed number. In the end, the program displays statistics: how many
# tries it took to guess the number, how long it took. Provide an exit by entering 0 if the user is
# tired of guessing the number.
