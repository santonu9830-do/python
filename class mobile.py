class Mobile:
    def __init__(self):
        self.__price = 15000

    def __mobileInfo(self):
        print("Mobile Information")

    def showPrice(self):
        self.__mobileInfo()
        print("Price:", self.__price)


mobile = Mobile()
mobile.showPrice()
