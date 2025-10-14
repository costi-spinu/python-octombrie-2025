# # # Task 1

# # # The user types in a number from 1 to 7 that represents a day of the week.
# # # Print its name. For example, if the number is 1,
# # # then you should display "Monday"; if 2, display "Tuesday," etc.


day_number = int(input("Enter a number (1-7):"))
days = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday",
}
if 1 <= day_number <= 7:
    print("The day is:", days[day_number])
else:
    print("Invalid number!")


# # # # Task 2
# # # # The user types in a number from 1 to 12 that represents a month.
# # # # Print its name. For example, if the number is 1, display "January"; if 2, display "February," etc


month_number = int(input("Enter a number (1-12): "))
months = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}
if 1 <= month_number <= 12:
    print("The month is:", months[month_number])
else:
    print("Invalid number! Please enter a number from 1 to 12.")


# # # Task 3
# # # The user types in a number. If the number is greater than 0,
# # # print "Your number is positive"; if it is less than zero,
# # # print "Your number is negative"; if it is equal to 0, print "Your number is equal to zero."

try:

    while True:
        number = int(input("Enter your number:"))
        if number < 0:
            print("Your number is negative.")
        elif number > 0:
            print("Your number is positive.")
        else:
            print("Your number is equal to zero.\nTry another number.")
        while True:
            again = input("\n Do you want to try again?(y/n):").strip().lower()
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
    print("Invalid input. Please enter a number")


# Task 4
# The user types in two numbers. Determine if these numbers are equal.
# If they are not, print them in ascending order.

try:
    while True:
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter the second number:"))
        if num1 == num2:
            print("numbers are equal")
        else:
            if num1 < num2:
                print("the number ascending order is:", f"{num1,num2}")
            else:
                print("the number ascending order is:", f"{num2,num1}")
        while True:
            again = input("\n Do you want to try again?(y/n):").strip().lower()
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
    print("Only numbers are allowed!!!")
