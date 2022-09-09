# 1. Write a recursive python function to print first N natural numbers.
def naturalNum(n):
    if n>0:
        naturalNum(n-1)
        print(n, end = ' ')

num = 10
naturalNum(num)
