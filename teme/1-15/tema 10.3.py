# Task 3
# Print the multiplication table in the user-specified range. If the user specified 3 and 5, the multiplication table might look like this:
# 3*1 = 3 3*2 = 6 3*3 = 9 … 3*10 = 30
# .....................................
# 5*1 = 5 5*2 = 10 5*3 = 15 … 5*10 = 50


num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
low = min(num1, num2)
high = max(num1, num2)

for i in range(low, high + 1):
    for j in range(low, high + 1):
        print(
            f"{i}*{j} = {i*j}", end="; "
        )  # am pus ; pentru citirea mai lizibila a textului printat in consola.
    print()


