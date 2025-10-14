# Task 2
# The user types in two numbers (start and end points of the range). Analyze all the numbers in this range. Print the following:
# 1.	All numbers in the range;
# 2.	All numbers in the range in descending order;
# 3.	All numbers that are multiples of 7;
# 4.	How many numbers are multiples of 5.


i = int(input("first number:"))
j = int(input("last number: "))
low = min(i, j)
high = max(i, j)
while True:
    choice = int(
        input(
            "Select option:\n\t 1.All numbers in the range;\n\t 2.All numbers in the range in descending order: \n\t 3.All numbers that are multiples of 7; \n\t 4.How many numbers are multiples of 5.\n\t 5.Exit\n"
        )
    )

    if choice == 1:
        print(f"All numbers in the range of {low} and {high} are:")
        for x in range(low, high + 1):
            print(x)
    elif choice == 2:
        print(f"All numbers in descending order are:\n")
        for x in range(high, low - 1, -1):
            print(x)
    elif choice == 3:
        print(f"All numbers multiple of 7 between {low} and {high} are:\n")
        for x in range(low, high + 1):
            if x % 7 == 0:
                print(x)
    elif choice == 4:
        count = 0
        for x in range(low, high + 1):
            if x % 5 == 0:
                count = count + 1
        print(f"Between {low} and {high} are", count, "numbers multiple of 5.")
    elif choice == 5:
        print("Goodbye!")
        exit()
    else:
        print("invalid number")
    while True:
        again = input("\n Do you want to try another option?(y/n):").strip().lower()
        if again == "y":
            break
        elif again == "n":
            print("See you!")
            exit()
        else:
            print("Invalid input, Please type'y' or 'exit' for yes or 'n' for no")
