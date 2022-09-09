# 9. Write a recursive python function to print first N multiples of a given number.
from numInput import numInput

def Nmultiple(n):
    given_Num = 2
    if n>0:
        Nmultiple(n-1)
        # print(given_Num,'*',n,'=',given_Num*n)
        print(given_Num*n)

num = numInput()
Nmultiple(num)