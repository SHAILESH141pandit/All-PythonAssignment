# 2. Write a recursive python function to calculate sum of first N odd natural numbers.

from numInput import numInput

# define function.
def sumoddnum(num):
    if num==1:
        return 1
    else:
        # if num%2!=0:
        n = (2*num-1) + sumoddnum(num-1)
        return n

# call numInput function.
x = numInput()

# calling sumoddnum
print(sumoddnum(x))