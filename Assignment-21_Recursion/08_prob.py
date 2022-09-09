# 8. Write a recursive python function to print cubes of first N natural numbers.
from numInput import numInput

def sqrof3(n):
    if n>0:
        sqrof3(n-1)
        print(n**3)

x = numInput()
sqrof3(x)