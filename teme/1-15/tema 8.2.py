# Task 2
# The user types in the length of a line and a symbol to fill the line. Print a vertical line made out of the typed in symbol of the specified length.
# For instance, if the typed in number and symbol are 5 and %, the output will be as follows:
# %
# %
# %
# %
# %

# Varianta for _
num = int(input("Enter a number for lenght:"))
sym = input("Enter symbol for printing the vertical:")

for c in range(num):
    print(sym)


# Varianta while _ loop
num = int(input("Enter a number for lenght:"))
sym = input("Enter symbol for printing the vertical:")
i = 0
while i < num:
    print(sym)
    i = i + 1
