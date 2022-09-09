# 3. Write a recursive python function to print first N odd natural numbers
def oddnatural_num(n):
    if n>0:
        oddnatural_num(n-1)
        if n%2!=0:
            print(n)
num = 10
oddnatural_num(num)
