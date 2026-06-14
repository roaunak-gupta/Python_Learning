
#! Example-2 ------------------------------------------------------------

class InsufficientBalanceError(Exception):
    pass

balance = 5000
withdrawal = 5500

try:
    if withdrawal > balance:
        raise InsufficientBalanceError("Not Enough Money.")

except InsufficientBalanceError as e:
    print(e)
finally:
    print(f"Your current balance : {balance}")
