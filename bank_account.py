# deposit(self, amount) - increases the account balance by the given amount
# withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
# display_account_info(self) - print to the console: eg. "Balance: $100"
# yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)

# Create a BankAccount class with the attributes interest rate and balance

# Add a deposit method to the BankAccount class

# Add a withdraw method to the BankAccount class

# Add a display_account_info method to the BankAccount class

# Add a yield_interest method to the BankAccount class

# Create 2 accounts

# To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)

# To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)

# NINJA BONUS: use a classmethod to print all instances of a Bank Account's info

class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance 
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
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

acct1 = BankAccount( 0.02, 160)
acct2 = BankAccount(0.25, 65200)


acct1.deposit(25).deposit(80).deposit(270).withdraw(35).yield_interest().display_account_info()

acct2.deposit(2100).deposit(150).withdraw(1600).withdraw(50).withdraw(100).withdraw(20).yield_interest().display_account_info()
