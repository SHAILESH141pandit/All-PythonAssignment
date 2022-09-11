# Write a recursive python function to calculate sum of squares of first N natural numbers.

from numInput import numInput

# define function.
def sqrOf_n(q):
    if q==1:
        return 1
    else:
        n = (q**2) + sqrOf_n(q-1)
        return n

# call numInput function.
d = numInput()

# calling sqrOf_n.
print(sqrOf_n(d))