# Task 3
# The user types in numbers. If the number is greater than 0, print "Your number is positive";
# if it is less than zero, print "Your number is negative"; if it is equal to 0, print
# "Your number is equal to zero." When the user types in 7, the program stops and prints "Good bye!"

while True:
    num = float(input("Enter a value:"))
    if num < 0:
        print("Your number is negative!")
    elif num > 0 and not num == 7:
        print("You're number is positive!")
    elif num == 7:
        print("Good Bye!")
        break
    else:
        print("You're number is equal to 0")
