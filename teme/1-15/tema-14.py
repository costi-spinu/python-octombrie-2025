print("Task 2")
import random

# generate two lists with random length and values
lung_lista1 = random.randint(10, 15)
lung_lista2 = random.randint(10, 15)

lista1 = [random.randint(-100, 100) for _ in range(lung_lista1)]
lista2 = [random.randint(-100, 100) for _ in range(lung_lista2)]

print("Lista 1:", lista1)
print("Lista 2:", lista2)

# 1. Third list containing elements of both lists
list_total = lista1 + lista2
print("\n1. Elemente din ambele liste:", list_total)

# 2. Third list without repetitions
list_no_duplicates = list(set(lista1 + lista2))
print("2. Elemente fără repetiții:", list_no_duplicates)

# 3. Third list containing elements common to both lists
list_common = list(set(lista1) & set(lista2))
print("3. Elemente comune ambelor liste:", list_common)

# 4. Third list containing elements unique to each list
list_unique = list(set(lista1) ^ set(lista2))   # symmetric difference
print("4. Elemente unice fiecărei liste:", list_unique)

# 5. Third list containing only smallest and largest values of each list
list_min_max = [min(lista1), max(lista1), min(lista2), max(lista2)]
print("5. Min/Max din fiecare listă:", list_min_max)