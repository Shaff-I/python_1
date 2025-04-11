class BankAccount:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit {amount} UAH. New balance: {self.balance} UAH")
        else:
            print("Deposit sum must be above zero!")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money.")
        elif amount <= 0:
            print("Withdraw sum must be above zero!")
        else:
            self.balance -= amount
            print(f"Withdrawed {amount} UAH. New balance: {self.balance} UAH")


myaccount = BankAccount("78445899234598", 1488)
myaccount.deposit(690)
myaccount.withdraw(1488)