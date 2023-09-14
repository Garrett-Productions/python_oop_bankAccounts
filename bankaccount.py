# class BankAccount:
#     balance = 0
    
#     def __init__(self, amount, int_rate):
#         self.amount = amount
#         self.int_rate = int_rate       # decimal format, 1% = .01
        
# When a new instance is created, if an amount is given, the balance of the account should initially be set to that amount; 
# otherwise, the balance should start at $0

class BankAccount:

    accountInfo = []

    def __init__(self, int_rate, balance=0 ): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accountInfo.append(self)


    def deposit(self, amount):                  #increases the account balance by the given amount
        self.balance += amount
        return self


    def withdraw(self, amount): #decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
        if self.balance < amount:
            print("Insufficient Funds")
            self.balance -= 5
        else:
            self.balance -= amount
            return self


    def display_account_info(self):
        print(f"Your Balance:${self.balance}.") #This is an F statement printing the current balance.
        return self


    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.int_rate * self.balance
        else:
            print("Sorry buddy your account needs to be above 0.")
        return self

    @classmethod
    def allInfo(cls):
        info = []
        
        for account in cls.accountInfo:
            info += account.display_account_info().yield_interest().deposit().withdraw()
            return info
            
            
            

        
#garrettsAccount = BankAccount(.07, 250)
#garrettsAccount.deposit(100).deposit(75).deposit(50).withdraw(75).display_account_info().yield_interest().display_account_info()

mattsAccount = BankAccount(.05, 100)
mattsAccount.deposit(50).deposit(175).withdraw(45).withdraw(60).withdraw(40).withdraw(80).yield_interest().display_account_info()
print(mattsAccount.accountInfo[]) #Im getting an error here but am submitting the assignment so I can follow the soluiton video


#We used default parameters above.
#My class method is close but going to critique with solution video.