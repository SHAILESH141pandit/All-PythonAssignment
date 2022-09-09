# 4. Write a recursive python function to print first N odd natural numbers in reverse order.
def oddReverse(n):
    if n>0:
        if n%2!=0:
            print(n)
        oddReverse(n-1)

num = 10
oddReverse(num)