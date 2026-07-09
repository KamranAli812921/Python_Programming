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
    

        