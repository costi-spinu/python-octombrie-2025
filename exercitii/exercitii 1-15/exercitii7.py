# # 1
# # The user types in two numbers. Print all the numbers in the specified range.

# i = int(input("Introdu primul numar:"))
# j = int(input("Introdu al doilea numar"))
# for k in range(i, j+1):
#     print(k)

# # 2
# # The user types in two numbers. Print all odd numbers in the specified range.

i = int(input("Introdu primul numar:"))
j = int(input("Introdu al doilea numar: "))
for k in range(i, j+1):
    if k % 2 ==0:
        print(k)


# # # 3
# # # The user types in two numbers. Print all even numbers in the specified range.

# # i = int(input("Introdu primul numar:"))
# # j = int(input("Introdu al doilea numar: "))
# # for k in range(i, j + 1):
# #     if k % 2 == 1:
# #         print(k)

# # 4
# # The user types in two numbers. Print all numbers in the specified range in descending order.

# i = int(input("Introdu primul numar:"))
# j = int(input("Introdu al doilea numar: "))
# if i > j:
#     stop = i
#     end = j
#     for k in range(stop, end - 1, -1):
#         print(k)

# elif i == j:
#     print("Nu exista niciun numar intre cele doua introduse")
# else:
#     for k in range(j, i - 1, -1):
#         print(k)


# # number1 = int(input(" primul nr:"))
# # number2 = int(input(" al doilea nr:"))
# # print(range(number1, number2, -1))
