# 8. Write a recursive python function to print binary of a given decimal number.

from numInput import numInput

# define function.
def fact(n):
    if n > 1:
        fact(n//2)
    print(n % 2, end='')


# call numInput function.
a = numInput()
# calling fact.
fact(a)
