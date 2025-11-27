# def doExercise1(var1):
#     def doExercise2(var2):
#         return var1**var2
#     return doExercise2

# functia2=doExercise1(3)
# print (functia2)
# print (functia2(2))


class UserPlayer:
    def __init__(self, name):
        self.name = name
        self.__walletSetter = (
            WalletFunctor()
        )  # a apelat __init__ din clasa WalletFunctor()
        self.__wallet = (
            self.__walletSetter()
        )  # a apelat __call__ din clasa WalletFunctor()

    def updateWallet(self, coins=0):
        self.__wallet = self.__walletSetter(coins)

    def showWallet(self):
        print(f"{self.name}! You have {self.__wallet} coins now.")


class UserPlayer:
    def __init__(self, name):
        self.name = name
        self.__wallet = 100

    def updateWallet(self, coins):
        self.__wallet += coins

    def showWallet(self):
        print(f"You have {self.__wallet} coins now.")


class WalletFunctor:
    def __init__(self, startCoins=100):
        self.__startCoins = startCoins

    def __call__(self, coins=0):
        return self.__startCoins + coins


user1 = UserPlayer("Joe")
print(user1.showWallet())  # se apeleaza init din class walletfunctor
user1.updateWallet(50)
user1.showWallet()
