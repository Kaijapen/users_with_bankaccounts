class BankAccount:
    # don't forget to add some default values for these parameters!
    account = []
    def __init__(self, int_rate = 0.0, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
        self.account.append(self)
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon

    def deposit(self, amount):
        # your code here
        self.balance += amount
        return self

    def withdraw(self, amount):
        # your code here
        self.balance -= amount
        return self

    def display_account_info(self):
        # your code here
        print(f'Balance: ${self.balance}')
        return self

    def yield_interest(self):
        # your code here
        if not self.balance < 0:
            self.balance *= self.int_rate
        return self

    @classmethod
    def display_all_accounts(cls):
        for account in cls.account:
            print(account.balance)


account1 = BankAccount(0.3, 1000)
account2 = BankAccount(0.15, 1500)
account1.deposit(450).deposit(300).deposit(75).withdraw(250).yield_interest()
account2.deposit(300).deposit(450).withdraw(250).withdraw(100).withdraw(75).withdraw(400).yield_interest()

BankAccount.display_all_accounts()