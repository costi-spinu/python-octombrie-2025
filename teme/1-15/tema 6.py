# Task 1
# The user types in a number from 1 to 100. If the number is a multiple of 3
# (divisible by 3 without remainder), print the word Fizz. If the number is a
# multiple of 5, print the wordBuzz. If the word is a multiple of 3 and 5, print
# Fizz Buzz. If the word is not a multiple of 3 and 5, print the number.

# If the user typed in a number out of the range, print an error message.

try:
    while True:
        number = int(input("Enter a number from 1 to 100:"))
        if number <= 100 and (number % 3 == 0 and number % 5 == 0):
            print("Fizz Buzz", end="\n")
            print("the number is multiple of 3 and 5")
        elif number <= 100 and (number % 3 == 0):
            print("Fizz", end="\n")
            print("the number is multiple of 3")
        elif number <= 100 and (number % 5 == 0):
            print("wordBuzz", end="\n")
            print("the number is multiple of 5")
        elif number <= 100 and not (number % 3 == 0 and number % 5 == 0):
            print("The number is not multiple of 3 or 5:", number)
        else:
            print("Erorr! The number is out of range")
        while True:
            again = input("\n Do you want to try again?(y/n/exit):").strip().lower()
            if again == "y":
                break
            elif again == "n":
                print("See you!")
                exit()
            elif again == "exit":
                print("bye bye!!!")
                exit()
            else:
                print("Invalid input, Please type'y' or 'exit' for yes or 'n' for no")
except ValueError:
    print("Error!You need to enter only numbers!")


# Task 2
# Write a program that, at the user's choice,
# raises the typed in number to the power of 0 through 7.


def raise_to_power(number, power):
    return number**power


def main():
    try:
        while True:
            number = float(input("Enter a number:"))
            power = int(input("Enter a power between 0 and 7:"))
            if 0 <= power <= 7:
                result = raise_to_power(number, power)
                print(number, "raised to the power of", power, "is", result)
            else:
                print("Please enter a power between 0 and 7")
                break
            while True:
                again = input("\n Do you want to try again?(y/n/exit):").strip().lower()
                if again == "y":
                    break
                elif again == "n":
                    print("See you!")
                    exit()
                elif again == "exit":
                    print("bye bye!!!")
                    exit()
                else:
                    print(
                        "Invalid input, Please type'y' or 'exit' for yes or 'n' for no"
                    )

    except ValueError:
        print("Please enter a valid number for call duration.")


if __name__ == "__main__":  # cod pentru rularea programului
    main()


# Task 3
# Write a program that calculates the cost of a
# call for different mobile phone operators. The user
#  types in the cost of the call and chooses operators for
# the outgoing and incoming calls. Print the cost.


try:

    while True:
        operator_prices = {"Orange": 0.10, "Telekom": 0.15, "Vodafone": 0.20}
        duration = float(input("Call duration (minutes): "))
        outgoing = input("Outgoing operator (Orange, Telekom, Vodafone): ")
        incoming = input("Incoming operator (Orange, Telekom, Vodafone): ")
        if outgoing not in operator_prices or incoming not in operator_prices:
            print("Invalid operator name. Please use: Orange, Telekom, or Vodafone.")
            break
        else:
            total = (operator_prices[outgoing] + operator_prices[incoming]) * duration
            print(f"Total call cost: {total:.2f} RON")

        while True:
            again = input("\n Do you want to try again?(y/n/exit):").strip().lower()
            if again == "y":
                break
            elif again == "n":
                print("See you!")
                exit()
            elif again == "exit":
                print("bye bye!!!")
                exit()
            else:
                print("Invalid input, Please type'y' or 'exit' for yes or 'n' for no")

except ValueError:
    print("Please enter a valid number for call duration.")
