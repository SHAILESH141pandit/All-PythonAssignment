# 2. Write a recursive python function to print first N natural numbers in reverse order.
def RnaturalNum(n):
    if n>0:
        print(n, end = ' ')
        RnaturalNum(n-1)

num = 10
RnaturalNum(num)
