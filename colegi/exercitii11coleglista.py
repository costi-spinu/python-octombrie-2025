# # task 2

# a = int(input("da mi nr"))
# for i in range(6):
#     if i < 3:
#         print((a * "*" + a * "_") * 4)
#     else:
#         print(((a * "*" + a * "_") * 4)[::-1])

# # task 1

a = input("da mi numar: ")
v = ["0", "sum", "average", "digits"]
print("optiunile sunt : ", *v)
o = input("da mi optiunea dorita")
match o.lower():
    case "0":
        k = 0
        for i in a:
            if int(i) == 0:
                k += 1
        print("numarul de 0 din {} este {}".format(a, k))
    case "sum":
        s = 0
        for i in a:
            s += i
        print("suma cifrelor este nr {} este {} ".format(a, s))
    case "average":
        c = 0
        for i in a:
            c = c * i
        print("produsul cifrelor nr {} este {}".format(a, c))
    case "digits":
        print("numarul de cifre al nr {} este {} ".format(a, len(a)))
    case _:
        print("optiune invalida")
