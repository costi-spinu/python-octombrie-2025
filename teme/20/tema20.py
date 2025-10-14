# Task 1
# Create a function that returns all odd numbers in a range.
# The function takes the beginning and the end of the range
# as parameters. Use the generator mechanism within the function.


def odd_numbers(start: int, end: int):
    low = min(start, end)
    high = max(start, end)
    for num in range(low, high + 1):
        if num % 2 != 0:
            yield num


for n in odd_numbers(3, 15):
    print(n, end=" ")

# Task 2
# Create a function that returns all values from a list that
#  are not in a range specified by a user. The function takes
#  the list, the beginning and the end of the range as parameters.
#  Use the generator mechanism within the function.


def values_outside_range(values, start, end):

    for v in values:
        if v < start or v > end:
            yield v


numbers = [2, 5, 8, 12, 15, 20, 25]
for val in values_outside_range(numbers, 10, 20):
    print(val, end=" ")
