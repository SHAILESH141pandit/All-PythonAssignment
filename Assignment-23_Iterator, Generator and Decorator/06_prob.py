# 6. Create a generator to produce first n prime numbers.

from numInput import numInput

# define function.
def isPrime(num):
    '''This function used to check given number is prime or not'''
    for i in range(2,num):
        if num%i==0:
            return False
    return True

# define function.
def prime_Generator(n):
    '''This function used to produce irst n prime numbers'''
    num = 2
    while n:
        if isPrime(num):
            yield num
            n-=1
        num+=1
    return

# calling numInput function.
nn = numInput()

# calling prime_Generator function.
it = prime_Generator(nn)

# driver code.
for i in it:
    print(i, end=' ')

# for new line.
print()