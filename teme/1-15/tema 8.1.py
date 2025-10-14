# Task 1
# The user types in two numbers. Find the sum of all even, odd numbers and multiples of 9 in the specified range, as well as arithmetic mean of each group.


try:
    while True:
        n1 = int(input("First number:"))
        n2 = int(input("Second number:"))
        low = min(n1, n2)
        high = max(n1, n2)

        even_numbers = []
        odd_numbers = []
        mult9_numbers = []

        for num in range(low, high + 1):
            if num % 2 == 0:
                even_numbers.append(num)

            else:
                odd_numbers.append(num)

            if num % 9 == 0:
                mult9_numbers.append(num)

        choice = input(
            f"Select which operation you want to be executed:\n\t 1. Sum of all even numbers between {low} and {high}? \n\t 2. Sum of all even odd numbers between {low} and {high}? \n\t 3. Multiple of 9 between {low} and {high}?\n\t 4. Arithmetic mean of each group? \n\t 5. Exit\n\t Enter your choice:"
        )
        if choice == "1":
            print(f"Even numbers:{even_numbers}")
            print(f"Sum:{sum(even_numbers)}")

        elif choice == "2":
            print(f"Odd numbers:{odd_numbers}")
            print(f"Sum:{sum(odd_numbers)}")
        elif choice == "3":
            print(f"Multiple of 9 numbers:{mult9_numbers}")
            print(f"Sum:{sum(mult9_numbers)}")
        elif choice == "4":
            print(
                f"\t Mean of even numbers:{sum(even_numbers)/ len (even_numbers)}\n\t Mean of odd numbers: {sum(odd_numbers)/len(odd_numbers)}\n\t Mean of multiply numbers of 9: {sum(mult9_numbers)/ len (mult9_numbers)}"
            )

        elif choice == "5":
            print("You're out! Goodbye!")
            break
        else:
            print("Invalid choide. Please select from 1 to 5.")
        while True:
            again = (
                input("\n Do you want to try again with another numbers?(y/n):")
                .strip()
                .lower()
            )
            if again == "y":
                break
            elif again == "n":
                print("See you!")
                exit()
            else:
                print("Invalid input, Please type'y' or 'exit' for yes or 'n' for no")


except ValueError:
    print("Incorect values!")
