# pricesUSD = [100.34, 35, 67.99, 25.5]
# print(pricesUSD)
# USDrate = 27.5


# def toPriceNew(priceList):
#     return list(map(lambda x: x * USDrate, priceList))


# def changePriceDecorator_v1(myFunction):
#     print("Hello! Let's change your prices...")

#     def simpleWrapper(argList):
#         print(
#             "I've got list of prices with {} elements. Function starts working...".format(
#                 len(argList)
#             )
#         )
#         resutl = myFunction(argList)
#         resutlwithDisc = list(map(lambda x: x * (1 - 0.15), resutl))
#         print("Let's set a discount..")
#         return resutlwithDisc

#     return simpleWrapper


# pricesToGRN = changePriceDecorator_v1(toPriceNew)
# print(toPriceNew(pricesUSD))


# @changePriceDecorator_v1
# def toPriceNew(priceList):
#     return list(map(lambda x: x*USDrate, priceList))
# print(toPriceNew(pricesUSD))

##########################################################################
# def methodDecorator(method_to_decorate):
#     def wrapper(self):
#         print("General information:")
#         method_to_decorate(self)
#     return wrapper

# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages

#     @methodDecorator
#     def showInfo(self):
#         print("Title: {}".format(self.title))
#         print("Author: {}".format(self.author))
#         print("Pages: {}".format(self.pages))

# book1 = Book("Python Crash Course", "Eric Matthes", 624)
# book1.showInfo()


class myDecorator:
    def __init__(self, fn):
        self.fn = fn

    def __call__(self, num1, num2):
        return self.fn(num1, num2) ** 2  # ridica la putere


@myDecorator
def addNums(x, y):
    return x + y


print(addNums(2, 3))  # 25
