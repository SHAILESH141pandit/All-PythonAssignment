# 10. Write a recursive python function to print a number in reverse order.
from numInput import numInput

def numb(n):
    if n>0:
        print(n)
        numb(n-1)

num = numInput()
numb(num)
