# 2. Create a generator to produce first n odd natural numbers.

from numInput import numInput
# define function.
def gen(n):
    a = 1
    while n:
        yield a
        a+=2
        n-=1

# calling numInput function.
nn = numInput()

# calling gen function.
it=gen(nn)

# driver code.
for  i  in it:
    print(i)