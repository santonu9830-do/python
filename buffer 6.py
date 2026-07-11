class BankAccount:
    def __init__(self):
        self.__balance = 5000

    def __accountInfo(self):
        print("Bank Account Details")

    def showBalance(self):
        self.__accountInfo()
        print("Balance:", self.__balance)


account = BankAccount()
account.showBalance()
