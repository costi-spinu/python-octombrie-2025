# Task 1
# Create a function that returns all Fibonacci numbers in a range.
# The function takes the beginning and the end of the range as parameters.

# Fibonacci numbers are a sequence of numbers where each successive
# number is the sum of the previous two numbers. The sequence begins
# with 0 and 1, and the next numbers are determined by the formula:
# F(0) = 0
# F(1) = 1
# F(n) = F(n-1) + F(n-2), for n > 1.
# The first few Fibonacci numbers are: 0, 1, 1, 1, 2, 3, 5, 8, 13,
# 21, 34, 55, 89, 144, 233, ...
# You can read more about the Fibonacci numbers.


def fibonacci_in_range(start: int, end: int):
    a, b = 0, 1
    while a <= end:  # Generate until we exceed the upper bound
        if a >= start:
            yield a
        a, b = b, a + b


for num in fibonacci_in_range(5, 50):
    print(num, end=" ")

# Task 2
# Create a function that returns the sum of the values of lists
# elements. The function accepts two lists.
# For example, if we have the following lists:
# 1 3 4 2
# 8 3 5 9
# The result would be:
# 9 6 9 11
# If the passed lists have different lengths the missing
# elements must be considered equal to zero.


def sum_lists(list1, list2):

    max_len = max(len(list1), len(list2))
    result = []
    for i in range(max_len):
        val1 = list1[i] if i < len(list1) else 0
        val2 = list2[i] if i < len(list2) else 0
        result.append(val1 + val2)
    return result


# Example usage:
a = [1, 3, 4, 2]
b = [8, 3, 5, 9]
print(sum_lists(a, b))  # Output: [9, 6, 9, 11]

# Example with different lengths:
c = [1, 2, 3]
d = [5, 6]
print(sum_lists(c, d))  # Output: [6, 8, 3]
