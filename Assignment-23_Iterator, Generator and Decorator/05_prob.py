# 05. Create a generator to produce first n terms of Fibonacci series.

from numInput import numInput

def sqrNumb(n_number):
    '''This function used to produce first n terms of Fibonacci series'''
    a,b=0,1
    while n_number:
        yield a
        a,b=b,a+b
        n_number-=1

# calling numInput function.
Inum = numInput()

# calling sqrNumb function.
it=sqrNumb(Inum)

# driver code.
for  i  in it:
    print(i)