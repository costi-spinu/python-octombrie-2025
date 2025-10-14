try:
    # Introducerea numerelor o singură dată
    num1 = int(input("Enter 1st number: "))
    num2 = int(input("Enter 2nd number: "))
    num3 = int(input("Enter 3rd number: "))

    while True:
        print(
            "\nChoose:"
            "\n1. Maximum number"
            "\n2. Minimum number"
            "\n3. Sum of numbers"
        )

        choice = int(input("Select an option (1-3): "))

        if choice == 1:
            result = max(num1, num2, num3)
            print("The maximum number is:", result)
        elif choice == 2:
            result = min(num1, num2, num3)
            print("The minimum number is:", result)
        elif choice == 3:
            result = num1 + num2 + num3
            print("The sum of the numbers is:", result)
        else:
            print("Invalid choice. Please choose between 1 and 3.\n")
            continue 
        while True:
            again = input("\nDo you want to return to the menu? (y/n): ").strip().lower()
            if again == 'y':
                break  # Revine la meniu
            elif again == 'n':
                print("Goodbye!")
                exit()
            else:
                print("Invalid input. Please type 'y' for yes or 'n' for no.")

except ValueError:
    print("Invalid input. Please enter only numbers.")