# Task 4
# Print a rhombus made out of asterisks.

n = int(input("Enter size (n >= 1): "))

for i in range(n):
    print(" " * (n - 1 - i) + "*" * (2 * i + 1))

for i in range(
    n - 2, -1, -1
):  # n-2 - pentru a sari o linie la baza rombului, -1 - pana unde se citeste din rand si -1 citire inversa
    print(" " * (n - 1 - i) + "*" * (2 * i + 1))
