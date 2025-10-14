# The user types in the size of the square's sides. '
# 'Print a solid square. The size is equal to the typed in square's
# side. Say the user typed in 3, the output will be as follows:
# ***
# ***
# ***


# size = int(input("Enter the size of the square: "))
# sign = input("Enter which sign you want:")
# semn = str(sign)
# for c in range(size):
#     print(semn * size)


# Task 2
# The user types in the width and height of a rectangle.
# Print a solid rectangle of the specified height and width.
# Say the user typed in the height equal to 3, and width 5,
# the output should be as follows:
# *****
# *****
# *****

# height = int(input("Enter the height of the rectangle: "))
# width = int(input("Enter the width of the rectangle: "))
# for c in range(height):
#     print("*" * width)


# # Task 3
# # The user types in the size of the square's sides.
# # Print an empty square (only its sides are displayed).
# # The side is equal to the typed in size.


# size = int(input("Enter the size of the square: "))
# for i in range(size):
#     if i == 0 or i == size - 1:
#         print("*" * size)
#     else:
#         print("*" + " " * (size - 2) + "*")

# Task 4
# The user types in the length and width of a rectangle.
# Print an empty rectangle (only its sides are displayed).
# The length and width are equal to the typed in numbers.


# # height = int(input("Enter the height of the rectangle: "))
# # width = int(input("Enter the width of the rectangle: "))

# # for i in range(height):
# #     if i == 0 or i == height - 1:
# #         print("*" * width)
# #     else:
# #         print("*" + " " * (width - 2) + "*")


income = float(input("Enter the annual income: "))

if income < 85528:
    tax = income * 0.18 - 556.02
# Write the rest of your code here.
elif income > 85528:
    dif = income - 85528
    tax = 14839.2 + (0.32 * dif)
if tax <= 0:
    tax = 0.0

tax = round(tax, 0)
print("The tax is:", tax, "thalers")
