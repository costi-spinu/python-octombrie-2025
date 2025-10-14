# print("------Task 1------")
# # Write a program that requests two integers x and y, and then calculates and prints the value of x raised to the power of y.

# x = int(input("Enter a number that will be x: "))
# y = int(input("Enter a number that will be y: "))
# print(f"The calculated value of {x} raised to the power of {y} is {x**y}")

# print("------Task 2------")
# # Count the number of integers in the range from 100 to 999 that have two identical digits.

# count = 0
# for i in range(100, 1000):
#     digit = str(i)
#     if (
#         digit[0] == digit[1] != digit[2]
#         or digit[0] == digit[2] != digit[1]
#         or digit[1] == digit[2] != digit[0]
#     ):
#         count += 1
# print(
#     f"The number of integers in the range from 100 to 999 that have two identical digits is: {count}"
# )

print("------Task 3------")
# # Count the number of integers in the range from 100 to 9999 that have different digits.

count = 0
for i in range(100, 10000):
    digits = str(i)
    if len(set(digits)) == len(digits):
        count += 1
print(
    f"the number of integers in the range from 100 to 9999 that have different digits is: {count}"
)

# print("------Task 4------")
# # The user types in an integer value. Remove all 3s and 6s from this integer and print it.

# num = input("Enter an integer: ")
# clean_num = "".join([digit for digit in num if digit not in "36"])
# print(f"Number after removing all 3s and 6s: {clean_num}")
