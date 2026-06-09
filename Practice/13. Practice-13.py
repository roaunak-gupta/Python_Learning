class Account:

    def __init__(self, balance, account):

        self.balance = balance

        self.account = account

    def credit(self, credit_balance):

        self.balance = self.balance + credit_balance

    def debit(self, debit_balance):

        self.balance = self.balance - debit_balance

    def print_balance(self):

        print(f"Your Account Balance : {self.balance}")


acc1 = Account(34000, 50526665706)

acc1.print_balance()
acc1.credit(2000)
acc1.print_balance()
acc1.debit(1000)
acc1.print_balance()
