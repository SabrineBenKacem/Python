class BankAccount:
    all_accounts = []

    # !<------------------Constructor----------------->
    def __init__(self, int_rate=0.02, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    # ! deposit method

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount is: {amount}$")
        return self

    # ! Withdraw Method
    def withdraw(self, amount):
        if self.balance < amount:
            self.balance -= 5
            print("Insufficient funds: Charging 5$")
            # print(f"Balance : {self.balance}$ ")
        else:
            self.balance -= amount
            print(f"We will di withdrawing {amount} for account")

    # ! display_account_info method

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    # ! yield_interest method
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self

    # !Ninja Bonus
    @classmethod
    def display_all_accounts(cls):
        for account in cls.all_accounts:
            print(f"Balance: {account.balance}\n, Interest rate: {account.int_rate}")