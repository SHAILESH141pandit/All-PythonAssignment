# 6. Write a python script to print first N even natural numbers.
n = int(input("Enter a number:  "))
i=1
while i<=n:
    if i%2==0:
        print(i)
    i+=1