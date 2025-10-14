# Task 1
# The user types in two numbers (start and end points of the range). Analyze all the numbers in this range as follows: if the number is a multiple of 7, print it.

# exercitiul 1
try:
    while True:
        i = int(input("Introdu primul numar:"))
        j = int(input("Introdu al doilea numar: "))
        print(f"multiple of 7 between {i} and {j} are:")
        if i < j:
            for k in range(i, j + 1):
                if k % 7 == 0:
                    print(k)
        elif i == j:
            print("no number found")
        else:
            for k in range(i, j - 1, -1):
                if k % 7 == 0:
                    print(k)
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
    print("Please enter only numbers.")

# exercitiul  2 (varianta scurta)

i = int(input("Introdu primul numar:"))
j = int(input("Introdu al doilea numar: "))

low = min(i, j)
high = max(i, j)
print("toate numerele multiple de 7 sunt:")
for k in range(low, high + 1):
    if k % 7 == 0:
        print(k)
