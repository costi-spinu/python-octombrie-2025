## random integeres
# import random

# lun_tup = random.randint(5, 10)
# t1 = tuple(random.randint(0, 10) for i in range(lun_tup))
# t2 = tuple(random.randint(0, 10) for i in range(lun_tup))
# t3 = tuple(random.randint(0, 10) for i in range(lun_tup))
# print("Tuple 1=", t1)
# print("Tuple 2=", t2)
# print("Tuple 3=", t3)
##verificare
t1 = (2, 2, 3, 4, 5)
t2 = (2, 5, 6, 7)
t3 = (2, 4, 5, 6)
print("Tuple 1=", t1)
print("Tuple 2=", t2)
print("Tuple 3=", t3)
# Task 1
# You have three tuples of integers. Find elements present in all tuples.
print("Task 1:")
element = []
for c in t1:
    if c in t2 and c in t3:
        element.append(c)
findetElement = set(element)
elementInAlltuples = tuple(findetElement)
print("Elements present in all tuples=:", elementInAlltuples)


# Task 2
# You have three tuples of integers. Find elements unique for each list.
print("Task 2:")
different = []
for d in t1:
    if d not in t2 and d not in t3:
        different.append(d)
differentWithoutRepeat = set(different)
differentNumbersInallTuples = tuple(differentWithoutRepeat)
print("All unique numbers =", differentNumbersInallTuples)


# Task 3
# You have three tuples of integers. Find elements that are present in each tuple and at the same position in each tuple.
print("Task 3:")
same = [x for x, y, z in zip(t1, t2, t3) if x == y == z]
print(
    "elements present in each tuple and at the same position in each tuple", tuple(same)
)


######functia zip
print("Functia zip")
a = (1, 2, 3)
b = (10, 20, 30)

for x, y in zip(a, b):
    print(x, y)
