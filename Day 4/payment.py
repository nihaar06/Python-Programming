class payment:
    def pay(self,amount):
        pass
class CashPayment(payment):
    def pay(self,amount):
        print(f"Paid Rs.{amount} in cash")
class CardPayment(payment):
    def pay(self,amount):
        print(f"Paid Rs.{amount} using credit/debit card")
class UPIPayment(payment):
    def pay(self,amount):
        print(f"Paid Rs.{amount} using UPI")
payments=[CashPayment(),CardPayment(),UPIPayment()]
for p in payments:
    p.pay(1000)