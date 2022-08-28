# 8. Write a python script to calculate sum of digits of a given number.
s = input("Enter a number:  ")
sum = 0
for i in s:
    sum = sum + int(i)
print("Sum of digits of a given number is",sum)