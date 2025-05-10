class BankAccount:
    def __init__(self, name, creditnumber, balance):
        self.name = name
        self.creditnum = creditnumber
        self.balance = balance

class Bank:
    def __init__(self, account, giveaccount):
        self.account = account
        self.giveaccount = giveaccount
        self.accountname = self.account.name
        self.accountcreditnum = self.account.creditnum

    def withdraw(self):
        withdrawmoney = float(input("How much money do you want to withdraw? "))
        if withdrawmoney >= 0 and withdrawmoney <= self.account.balance:
            self.account.balance -= withdrawmoney
        else:
            print("ERROR 420 you can't withdraw more than there is!")
        print("=" * 48)
        print(f"            {self.account.creditnum}")
        print(f"Name: {self.account.name}")
        print(f"balance: {self.account.balance}")
        print("=" * 48)

    def add(self):
        addmoney = float(input("How much money do you want to add? "))
        self.account.balance += addmoney
        print("=" * 48)
        print(f"            {self.account.creditnum}")
        print(f"Name: {self.account.name}")
        print(f"balance: {self.account.balance}")
        print("=" * 48)

    def give(self):
        givemoney = float(input("How much money do you want to give? "))
        if 0 <= givemoney <= self.account.balance:
            self.account.balance -= givemoney
        else:
            print("ERROR 420 you can't give more than you have!")
        self.account.balance -= givemoney
        self.giveaccount.balance += givemoney
        print("=" * 48)
        print(f"            {self.account.creditnum}")
        print(f"Name: {self.account.name}")
        print(f"balance: {self.account.balance}")
        print("=" * 48)
        print("=" * 48)
        print(f"            {self.giveaccount.creditnum}")
        print(f"Name: {self.giveaccount.name}")
        print(f"balance: {self.giveaccount.balance}")
        print("=" * 48)

account1 = BankAccount("Nasser", 18746573821820347, 14888.0)
account2 = BankAccount("Katya", 87929782614681623, 148.88)
privatbank = Bank(account1, account2)
privatbank.withdraw()
privatbank.add()
privatbank.give()