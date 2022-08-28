# 1. Write a python script to calculate sum of first N natural numbers.
sum =0
for i in range(int(input("Enter a number: "))):
    sum=sum+(i+1)
print("Sum of first N natural numbers is",sum)