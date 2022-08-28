# 6. Write a python script to calculate factorial of a given number.
Facto = 1
for i in range(1,int(input("Enter a number:  "))+1):
    Facto = Facto*i
print("Factorial of a given number is",Facto)