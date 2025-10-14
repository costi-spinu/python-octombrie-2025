# # Popa Ovidiu


# # task2

# n = int(input("da mi dimensiune lista"))
# d = 0
# lista = []
# c = int(input("da mi nr: "))
# for i in range(n):
#     b = int(input("da mi nr: "))
#     lista.append(b)
# for i in lista:
#     if i == c:
#         d += 1
# print("numarul {} se regaseste in lista {} de {}".format(c, lista, d))

# # task 1

# import string

# txt = input("da mi text")
# txt2 = txt.title()
# cf = txt.count(string.digits)
# pct = txt.count(string.punctuation())
# excl = txt.count("!")
# print(
#     "textul cu cuvinte cu prima litera capitalised este {}\nnumarul de cifre este {}\nnumarul de semne de punctuatie este {}\n iar numarul de semne de exclamatie este {} ".format(
#         txt2, cf, (pct + pct1), excl
#     )
# )

# # task3
# n = int(input("da mi dimensiune lista"))
# lista = []
# for i in range(n):
#     b = int(input("da mi nr: "))
#     lista.append(b)
# s = sum(i for i in lista)
# avg = s / n
# print("suma numerelor din lista este {},\n iar media lor este {}".format(s, avg))
