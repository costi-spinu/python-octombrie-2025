# number = int(input("Enter a number:"))
# if number % 2 == 0:
#     print(f"{number} is an Even number.")
# else:
#     print(f"{number} is an Odd number.")


# number = int(input("enter the number:"))
# if number % 7 == 0:
#     print("Your number is a multiple of 7.")
# else:
#     print("Your number is not a multiple of 7")


# num1 = float(input())
# num2 = float(input())

# maximum = max(num1, num2)
# print("the maximum number is:", maximum)


# num1 = float(input())
# num2 = float(input())

# minimum = min(num1, num2)
# print("the maximum number is:", minimum)

num1 = float(input("primul numar"))
num2 = float(input("al doilea numar"))

print("Alege o operatie:\n1.suma\n2.diferenta\n3.impartire\n4.aritmetica")
choice = input("introdu un numar(1-4):")

if choice == "1":
    result = num1 + num2
    print("The sum is:", result)
elif choice == "2":
    result = num1 - num2
    print("the difference is:", result)
elif choice == "3":
    result = num1 * num2
    print("the product is:", result)

elif choice == "4":
    result = (num1 + num2) / 2
    print(f"The arithmetic mean is: {result}")

else:
    print("invalid choice")


# a = int(input("Introdu primul numar: "))
# b = int(input("Introdu al doilea numar: "))
# optiune = input(
#     "Alege optiunea pe care vrei sa o afisez:\n1. Suma\n2. Diferenta\n3. Produs\n4. Media aritmetica\n"
# )
# suma = a + b
# diferenta = a - b
# produs = a * b
# medie = (a + b) / 2
# match optiune:
#     case "1":
#         print(suma)
#     case "2":
#         print(diferenta)
#     case "3":
#         print(produs)
#     case "4":
#         print(medie)
#     case _:
#         print("Nu ai introdus o optiune valida")
