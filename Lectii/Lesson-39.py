def doExercise1(var1):
    print("a fost apelata metoda doExercise1")

    #
    def doExercise2(var2):
        return var1**var2

    return doExercise2


functia2 = doExercise1(3)
print(functia2)


#####DECORATORI
class myDecorator:
    def __init__(self, fn):
        self.fn = fn

    def __call__(self, num1, num2):
        return self.fn(num1, num2) ** 2


@myDecorator
def addNums(x, y):
    return x + y


print(addNums(2, 3))


####functii de getter si setter si metode magice!

# class Product:
#     def __init__(self,name,price,discountPercentage=25):
#         self.name=name
#         self.price=price
#         self.discountPercentage=discountPercentage

# @property
# def discountPercentageXYZ(self):
#     return self.discountPercentage

# @discountPercentageXYZ.setter
