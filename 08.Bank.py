class bank:
    balance=0
    def __init__(self,name,amount):
        self.name=name
        self.amount=amount
        print(f"The account was created for {self.name}")
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        self.balance-=amount
    def showBalance(self):
        print(f"The current Balance is {self.balance}")
kamran=bank('Kamran Ali',2000)
kamran.deposit(2000)
kamran.showBalance()
kamran.withdraw(200)
kamran.showBalance()
        