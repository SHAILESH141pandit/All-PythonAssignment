# 6. Write a recursive python function to calculate the factorial of a number.

from numInput import numInput

# define function.
def fact(z):
    if z==1:
        return 1
    else:
        n = z * fact(z-1)
        return n

# call numInput function.
a = numInput()

# calling fact.
print(fact(a))