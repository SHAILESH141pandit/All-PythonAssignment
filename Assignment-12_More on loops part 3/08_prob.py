# 8. Write a python script to print first N terms of a Fibonacci series.
n = int(input("Enter a number:  "))
a = 0
b = 1
print(a)
print(b)
for i in range(2,n):
    fub = a + b
    a = b
    b = fub
    print(fub)