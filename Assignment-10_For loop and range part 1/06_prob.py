# 6. Write a python script to print first N even natural numbers.
for i in range(1,int(input("Enter a number:  "))+1):
    if i%2==0:
        print(i)