class Bank_Account:
    def __init__(self):
        self.balance=0
        
        
 
    def deposit(self):
        amount=float(input())
        self.balance += amount
        
 
    def withdraw(self):
        amount = float(input())
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")
 
    

s = Bank_Account()
s.deposit()
s.withdraw()
