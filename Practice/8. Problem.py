# This is a program to show the factorial of a number.

def cal_fact(value):
    fact = 1
    for i in range(1, value+1):
        fact *= i
    print(fact)


n = input("Enter your Number for factorial : ")
cal_fact(int(n))
