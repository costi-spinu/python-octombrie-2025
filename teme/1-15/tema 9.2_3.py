#  Task 2
# Count the number of integers in the range from 100 to 999 that have two identical digits.
#  var1
count = 0

for x in range(100, 1000):
    digits = str(x)
    a, b, c = digits[0], digits[1], digits[2]
    if (a == b != c) or (a == c != b) or (b == c != a):
        count = count + 1

print("Count of numbers with exactly two identical digits:", count)
# var2

count = 0

for x in range(100, 1000):
    digits = str(x)  # str - conversteste sirul de numere in strinng
    # num_dif = set(digits) - sed digit imi elimina numerele identice,
    # iar len din set imi numara sirul (in cazul asta rezultatul va fi 2 si 3 ,
    # - 2 pentru cele care au nr identic si a fost eliminat prin comanda set)
    if len(set(digits)) == 2:  # am eliminat astfel numerele care nu sunt identice
        count = count + 1

print("Count of numbers with exactly two identical digits:", count)


# Task 3
# Count the number of integers in the range from 100 to 9999 that have different digits.
count = 0

for num in range(100, 10000):
    digits = str(num)  # str - conversteste sirul de numere in strinng
    if len(set(digits)) == len(
        digits
    ):  # comanda set elimina duplicatele din numere , iar comanda len - da lungimea numarului
        count = count + 1


print("Count of numbers with all different digits from 100 to 9999:", count)
