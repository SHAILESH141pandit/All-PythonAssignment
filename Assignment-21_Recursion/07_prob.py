# 7. Write a recursive python function to print squares of first N natural numbers
from numInput import numInput

def sqr(n):
    if n>0:
        sqr(n-1)
        print(n**2)

num = numInput()
sqr(num)