from bankaccount import BankAccount

class User:
    def __init__(self, balance_savings, balance_checking, name):
        self.balance_savings = balance_savings
        self.balance_checking = balance_checking
        self.name = name
        self.savings = BankAccount(int_rate = 0.02, balance = balance_savings)
        self.checking = BankAccount(int_rate = 0.02, balance = balance_checking)
    
    def make_withdrawal(self, amount, account):
        account.withdraw(amount)
        return self
    
    def display_user_balance(self, account):
        print(f"User: {self.name}, Balance: {account.balance}" )
    
    def make_deposit(self, amount, account):
        account.deposit(amount)
        return self

    def transfer_money(self, other_user, account, amount):
        account.withdraw(amount)
        other_user.savings.deposit(amount)
        return self

if __name__ == '__main__':
    kaija = User(10000, 8500,"Kaija")
    jonathan = User(8000, 5000,"Jonathan")
    juan = User(12000, 1500, "Juan")
    kaija.make_deposit(500, kaija.savings).make_deposit(200, kaija.checking).make_deposit(100, kaija.savings).make_withdrawal(1000, kaija.checking).display_user_balance(kaija.checking)
    jonathan.make_deposit(600, jonathan.checking).make_deposit(150, jonathan.savings).make_withdrawal(400, jonathan.savings).make_withdrawal(150, jonathan.checking).display_user_balance(jonathan.savings)
    juan.make_deposit(500, juan.checking).make_withdrawal(150, juan.savings).make_withdrawal(1000, juan.checking).make_withdrawal(50, juan.savings).display_user_balance(juan.checking)
    kaija.transfer_money(juan, kaija.checking, 5000).display_user_balance(kaija.savings)
    juan.display_user_balance(juan.savings)