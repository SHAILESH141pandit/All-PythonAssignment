# 2. Write a python script to check whether a given number is Prime or not.
num = int(input("Enter a number:  "))
for i in range(2,num):
    if num%i==0:
        print("Given number is not Prime")
        break
else:
    print("Given number is Prime")