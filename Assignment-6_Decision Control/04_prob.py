''' 4. Write a python script to print greater between two numbers. Print number only once
    even if the numbers are the same.
'''
num1 = int(input("Enter a first number:  "))
num2 = int(input("Enter a second number:  "))

if num1>num2:
    print("First number is grater then Second number: ","First:",num1,"Second:", num2)

elif num2>num1:
    print("Second number is grater then First number: ","First:",num1,"Second:", num2)
    
elif num1==num2:
    print("Number is same: ",num1)
    
else:
    print("Please Enter only number.")