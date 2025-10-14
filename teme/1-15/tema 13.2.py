# Task 2
# You have a list of integers filled with random numbers.
# Find the largest and the smallest elements, count negative
# and positive elements, as well as zeros. Print the results.

##list1 = [i*i for i in range(6)] - generator de lista
##print(list1) #[0, 1, 4, 9, 16, 25]
## in loc de i*i - avem random.randint(-10,10) - sa adauge numere aleatorii

print("Task 2")
import random

lun_lista = random.randint(2, 10)
print("atribuire aleatorie pentru lungime lista:", lun_lista)
numbers = [random.randint(-10, 10) for c in range(lun_lista)]
print("Lista de numere creata:", numbers)
##1 the largest number
high = max(numbers)
print("The largest number from the created list is:", high)
##2 the smallest number
low = min(numbers)
print("The smallest number from the created list is:", low)
##3 count positive numbers
positiveNumbers = sum(1 for n in numbers if n > 0)
print(f"There are {positiveNumbers} positive number(s)")
##4 count negative numbers
negativeNumbers = sum(1 for n in numbers if n < 0)
print(f"There are {negativeNumbers} negative number(s)")
##5 count zeros
zeros = sum(1 for n in numbers if n == 0)
print(f"There are {zeros} zero(s)")
