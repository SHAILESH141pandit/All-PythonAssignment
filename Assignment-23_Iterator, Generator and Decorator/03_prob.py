# 3. Create a generator to produce first n even natural numbers.

from numInput import numInput

def evenNum(n):
    '''This function used to produce first n even natural numbers'''
    num = 2
    while n:
        yield num
        num+=2
        n-=1

# calling numInput function.
Inum = numInput()

# calling evenNum function.
it=evenNum(Inum)

# driver code.
for  i  in it:
    print(i)