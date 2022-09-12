# 4. Create a generator to produce squares of first N natural numbers.

from numInput import numInput

def sqrNumb(n_number):
    '''This function used to produce squares of first N natural numbers'''
    for  i in range(1,n_number+1):
        yield i**2

# calling numInput function.
Inum = numInput()

# calling sqrNumb function.
it=sqrNumb(Inum)

# driver code.
for  i  in it:
    print(i)