from bank_account import BankAccount
# !------------------ User
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(0.02, 0)
        self.saving_account = BankAccount(0.01, 750)

    def make_deposit(self, amount, acc="main"):
        if acc == "main":
            self.account.deposit(amount)
        elif acc == "saving":
            self.saving_account.deposit(amount)
        return self

    def make_withdrawal(self, amount, acc="main"):
        if acc == "main":
            self.account.withdraw(amount)
        elif acc == "saving":
            self.saving_account.withdraw(amount)
        return self

    def display_user_balance(self, acc="main"):
        if acc == "main":
            print(self.account.balance)
        elif acc == "saving":
            print(self.saving_account.balance)
        return self


user1 = User("John", "john@gmail.com")

user1.make_deposit(1000).make_withdrawal(150).display_user_balance()
user1.make_deposit(500, "saving").make_withdrawal(300, "saving").display_user_balance(
    "saving"
)
