# Task 1
# Print all prime numbers in the user-specified range. A number is prime if it is divisible only by itself and by one. For instance, 3 is a prime number, but 4 is not.


try:
    while True:
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))
        low = min(num1, num2)
        high = max(num1, num2)
        primes = []
        nonprimes = []
        print("Enter which operation you want to do:")
        print(f"\t1.show prime numbers from {low} to {high}")
        print(f"\t2.show wich numbers are not prime from {low} to {high}")
        print(f"\t3.Enter other range")
        print(f"\t4.Exit")
        choice = int(input("Enter you're choice (1-4):"))

        if choice == 1:
            print("Prime numbers:")
            for c in range(low, high + 1):
                if c > 1:
                    for i in range(2, c):
                        if c % i == 0:
                            break
                    else:
                        primes.append(c)
            print(primes)
            print(f"there are {len(primes)} prime numbers ")

        elif choice == 2:
            print("Non prime numbers are:")
            for c in range(low, high + 1):
                if c > 1:
                    for i in range(2, c):
                        if c % i == 0:
                            nonprimes.append(c)
                            break
                    else:
                        primes.append(c)
            print(nonprimes)
            print(f"there are {len(nonprimes)} nonprime numbers ")

        elif choice == 3:
            print("Please insert 2 numbers for another range")
            continue

        elif choice == 4:
            print("Goodbye")
            exit()
        else:
            print("Invalid input!")

        while True:
            again = (
                input("\tDo you want to try again with another numbers?(y/n):")
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
    print("Invalid output!")
