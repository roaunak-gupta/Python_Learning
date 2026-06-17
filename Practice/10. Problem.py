def sum_of_natural_num(n):
    if (n == 0):
        return 0
    return sum_of_natural_num(n-1) + n
    


sum = sum_of_natural_num(52)
print(sum)
