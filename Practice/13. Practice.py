class Account:

    def __init__(self, balance, account):

        self.balance = balance
        self.account = account

    def credit(self, credit_balance):

        self.balance = self.balance + credit_balance
        print(
            f"Rs. {credit_balance} was credited from account no. {self.account}\n")

    def debit(self, debit_balance):

        self.balance = self.balance - debit_balance
        print(
            f"Rs. {debit_balance} was debited from account no. {self.account}\n")

    def print_balance(self):

        print(f"Your Account Balance : {self.balance}\n")


acc1 = Account(34000, 50526665706)

while True:
    print("Enter your Mode (CR = Credit & DR = Debit & PR = Print your Balance)")
    intp = input("Enter your Mode : ")
    if (intp == "CR"):
        cr = input("Enter your Amount to Credit : ")
        acc1.credit(int(cr))
    elif (intp == "DR"):
        dr = input("Enter your Amount to Debit : ")
        acc1.debit(int(dr))
    elif (intp == "PR"):
        acc1.print_balance()
    else:
        print("You Enter the wrong Mode. Try Again...\n")
        continue
