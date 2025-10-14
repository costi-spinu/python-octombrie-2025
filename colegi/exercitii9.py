# task1
numar = int(input("Introdu un numar pentru care să afisez tabla inmultirii: "))

for i in range(1, 11):
    print(f"{numar} * {i} = {numar * i}")

# task2
print("Convertor valutar")
print("1. EUR -> RON")
print("2. RON -> EUR")

optiune = input("Alege optiunea (1 sau 2): ")

if optiune == "1":
    suma = float(input("Introdu suma in EUR: "))
    print(f"{suma} EUR = {suma * 5:.2f} RON")
elif optiune == "2":
    suma = float(input("Introdu suma in RON: "))
    print(f"{suma} RON = {suma / 5:.2f} EUR")
else:
    print("Optiune invalida")

# task3
start = int(input("Inceputul intervalului: "))
end = int(input("Sfarsitul intervalului: "))

while True:
    numar = int(input("Introdu un numar sa verific daca apartine intervaluluio: "))
    if start <= numar <= end:
        break
    print("Numarul nu e în interval. Incearca altul")

for i in range(start, end + 1):
    if i == numar:
        print(f"!{i}!", end=" ")
    else:
        print(i, end=" ")

# task4
import random
import time

numar = random.randint(1, 500)
incercari = 0

start_time = time.time()

while True:
    guess = int(input("Introdu un numar ( introdu 0 pentru a termina jocu ): "))

    if guess == 0:
        print("Iesire joc... Numarul era:", numar)
        break

    incercari = incercari + 1

    if guess == numar:
        durata = time.time() - start_time
        print(f"Ai ghicit numarul!")
        print("Numar incercari: ", incercari)
        print(f"Timp: {durata:.2f} secunde")
        break
    elif guess < numar:
        print("Nr e mai mare.")
    else:
        print("Nr e mai mic.")
