class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance 

    def deposit(self, amount):
        self.balance += amount
        print("Deposit Amount:", amount)
        return self
    
    def withdraw(self, amount):
        if self.balance >=amount:
            self.balance -= amount
            print ("Withdraw:", amount)
            return self
        else:
            self.balance = self.balance-5
            print("Insufficient Funds")
            return self

    def display_account_info(self):
        print("Balance:", self.balance)
        print("Interest Rate:", self.int_rate)
        return self

    def yield_interest(self):
        self.balance = (self.balance * self.int_rate) + self.balance
        return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=200)
    
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    
    def display_user_balance(self):
        self.account.display_account_info
        return self

user1 = User("Ninja", "ninja@dojo.com")

user1.make_deposit(25)