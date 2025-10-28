### Functie recursiva


# def recursive_sum(a, b):
#     if a == b:
#         return a
#     return a + recursive_sum(a + 1, b)


# # 1+2+3+4+5

# print(recursive_sum(1, 5))

#####3.2. Anonymous lambda Functions

# def add10(x):
#     return x + 10

# myNumbers = [2, 2.5, 4.56, 23]
# newNum = lambda x:x + 10
# for num in myNumbers:
#     print(newNum(num))


# myNumbers = [2, 2.5, 4.56,23]
# for num in myNumbers:
#     print((lambda x:x + 10)(num))