class BankAccount:
    def __init__(self,balance=0):
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
    def withdraw(self,amount):
        if self.__balance>amount:
            self.__balance-=amount
    def get_balance(self):
        return self.__balance
acc1=BankAccount()
acc1.deposit(5000)
acc1.withdraw(2000)
print(acc1.get_balance())