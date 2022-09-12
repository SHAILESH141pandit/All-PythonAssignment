# Write a recursive python function to calculate sum of first N even natural numbers.

from numInput import numInput

# define function.
def evenSum_num(num):
    if num==1:
        return 2
    else:
        n = (2*num) + evenSum_num(num-1)
        return n

# call numInput function.
d = numInput()

# calling evenSum_num.
print(evenSum_num(d))