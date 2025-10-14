# Task 1
# Calculate the following in a list filled with random numbers:
# Sum of negative numbers;
# Sum of even numbers;
# Sum of odd numbers;
# Product of elements with indices divisible by 3;
# Product of elements between the smallest and the largest element;
# The sum of the elements between the first and the last positive elements.

import random

lun_lista = random.randint(2, 10)
numbers = [random.randint(-10, 10) for c in range(lun_lista)]
print(numbers)
sum_neg = sum(i for i in numbers if i < 0)
print("suma numerelor negative", sum_neg)
sum_even = sum(i for i in numbers if i % 2 == 0)
print("Suma numerelor pare:", sum_even)
sum_odd = sum(i for i in numbers if i % 2 != 0)
print("Suma numerele impare:", sum_odd)
list2 = []
for i in numbers:
    if i % 3 == 0:
        list2.append(i)
print(list2)
inmultirelist2 = (i * i for i in list2)

print(inmultirelist2)

# prod_div_index_3 = 1
# for idx in range(0, len(numbers), 3):
#     prod_div_index_3 *= numbers[idx]
# print("Inmultirea elementelor cu indici divizibili cu 3:", prod_div_index_3)


# Task 2
# There is a list of integers filled with random numbers. Do the following based on this data:
# Create a list of integers containing only even numbers;
# Create a list of integers containing only odd numbers;
# Create a list of integers containing only negative numbers;
# Create a list of integers containing only positive numbers.

import random

# List of 10 random integers between -10 and 10
lst = [random.randint(-10, 10) for _ in range(10)]
# lista de numere pare
print(lst)
print("\n")
lst1 = []
for num in lst:
    if num % 2 == 0:
        lst1.append(num)
print(lst1)
print("\n")
# lista de numere impare
lst2 = []
for num in lst:
    if num % 2 != 0:
        lst2.append(num)
print(lst2)
print("\n")
# lista de nr negative:
lst3 = []
for num in lst:
    if num < 0:
        lst3.append(num)
print(lst3)
print("\n")
# lista de numere pozitive:
lst4 = []
for num in lst:
    if num > 0:
        lst4.append(num)
print(lst4)
