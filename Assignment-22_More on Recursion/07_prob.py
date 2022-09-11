# 7. Write a recursive python function to calculate sum of the digits of a given number.

from numInput import numInput

# define function.
def fact(num):
    if num==0:
        return 0
    else:
        x = (num%10) + fact(num//10)
        return x

# call numInput function.
a = numInput()

# calling fact.
print(fact(a))