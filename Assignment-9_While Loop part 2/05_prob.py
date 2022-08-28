# 5. Write a python script to print first N odd natural numbers in reverse order
n = int(input("Enter a number:  "))
y=0
while y<n:
    if y%2!=0:
        print(n-y)
    y+=1