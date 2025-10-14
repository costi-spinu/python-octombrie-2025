# Task 1
# Write a recursive function for finding the greatest common divisor of two integers.


def cd(a, b):
    if b == 0:
        return a
    else:
        return cd(b, a % b)


print(cd(6, 9))
