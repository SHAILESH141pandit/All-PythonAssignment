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


# def binary(n):
#    """Function to print binary number
#    for the input decimal using recursion"""
#    if n > 1:
#        binary(n//2)
#    print(n % 2,end = '')
 
# # Take decimal number from user
# dec = int(input("Enter an integer: "))
# binary(dec)