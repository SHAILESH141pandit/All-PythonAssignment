# 6. Write a recursive python function to print first N even natural numbers in reverse order.
from numInput import numInput

def even_reverseNum(a):
    if a>0:
        if a%2==0:
            print(a)
        even_reverseNum(a-1)

num =numInput()
even_reverseNum(num)