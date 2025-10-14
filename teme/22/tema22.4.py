# Task 4
# Implement the third task through a function.
#  The function should take a list as an argument and
# return the sum of the list elements. The correctness
# check should be inside the function. Create two versions
# of the function implementation:
# The first version does not handle the exception inside
# the function. All processing is outside the function;
# The second version handles the exception inside the function.


def suma_lista(lista):
    if not isinstance(lista, list):
        raise TypeError("Argumentul trebuie sa fie o lista")
    if not all(isinstance(x, (int, float)) for x in lista):
        raise ValueError("Toate elementele listei trebuie sa fie numere")
    return sum(lista)


valori = []
print("Introdu numere pozitive si scrie 'gata' cand ai terminat:")

while True:
    num = input("Numar: ")
    if num.lower() == "gata":
        break
    try:
        numere = int(num)
        if numere <= 0:
            raise ValueError("Doar numere pozitive")
        valori.append(numere)
    except ValueError as e:
        print(f"Eroare: {e}")


if valori:
    print(f"Lista numerelor introduse: {valori}")
    print("Suma este:", suma_lista(valori))
else:
    print("Nu ai introdus niciun numar valid.")
