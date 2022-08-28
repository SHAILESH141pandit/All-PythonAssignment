# 4. Write a python script to calculate sum of first N odd natural numbers.
osum = 0
for a in range(1,int(input("Enter a number:  "))+1):
    if a%2!=0:
        osum+=(a)
print("Sum of first N odd natural numbers is",osum)
    