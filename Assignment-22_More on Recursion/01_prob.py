# 1. Write a recursive python function to calculate sum of first N natural numbers.

from numInput import numInput

# define function for print sum of n nanutal numbers.
def sumof_num(n):
    if n==1:
        return 1
    else:
        r = n + sumof_num(n-1)
        return r

# calling number input function.
num = numInput()
# functin call
print(sumof_num(num))