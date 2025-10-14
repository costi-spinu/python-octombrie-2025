# Task 1
# The user types in a number. Determine how many digits this number has,
# find their sum and average. Determine how many zeros this number has.
# Implement a dialog with the user through a menu.


try:
    while True:
        num = int(input("Enter number:"))
        print("\t1.Determine how many digits this number has")
        print("\t2.Sum from digits")
        print("\t3.Average from digits")
        print("\t4.Determine how many zeros this number has")
        print("\t5.Exit")
        choice = int(input("\tPlease select from 1-6:\n"))
        if choice == 1:
            c = str(abs(num))
            print("Numbers digits:", len(c))

        elif choice == 2:
            di = [int(d) for d in str(abs(num))]  # abs- pentru numerele negative
            print(f"Sum numbers from {num}:", sum(di))

        elif choice == 3:
            di = [int(d) for d in str(abs(num))]  # am creat o lista di
            avg = sum(di) / len(di)
            print(f'Average number from "{num}" is:', avg)

        elif choice == 4:
            zero = str(num).count("0")
            print(f'Number of zeros from "{num}" is:', zero)

        elif choice == 5:
            print("Goodbye!")
            break

        while True:
            again = (
                input("\tDo you want to try again with another number?(y/n):")
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
    print("\nError! Please enter a number from 1-6")
