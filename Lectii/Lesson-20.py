# customers = ['AdminJane', 'adminBob', 'STUDENTbob', 'studentAlice', 'Kate']
# def sayHello(customer:str):
#     if customer.find("admin") != -1:
#         print("Hello, admin - {}".format(customer))
#     elif customer.find("student") != -1:
#         print("Hello, student - {}".format(customer))
#     else:
#         print("Hello, {}".format(customer))

# def greetings(customList:list, greetF):
#     for customer in customList:
#         greetF(customer.lower())
# greetings(customers, sayHello)


def discount10(price, voucher):
    return price - price * 10 / 100 - voucher


def discount15(price, voucher):
    return price - price * 15 / 100 - voucher


def discount20(price, voucher):
    return price - price * 20 / 100 - voucher


def userChoice(c):
    if c == "1":
        return discount10
    elif c == "2":
        return discount15
    elif c == "3":
        return discount20


price = 1000
voucher = 20
for i in range(3):
    userAncw = input("Your choice:")
    myCalculation = userChoice(userAncw)
    print(myCalculation(price, voucher))
