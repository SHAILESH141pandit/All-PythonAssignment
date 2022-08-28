''' 10. Write a python script to print greater among three numbers. Print number only once
even if the numbers are the same. '''

num1 = int(input("Enter a first number:  "))
num2 = int(input("Enter a second number:  "))
num3 = int(input("Enter a third number:  "))

if num1>num2>num3:
    print("grater number is: ",num1)

elif num2<num1<num3:
    print("grater number is: ",num3)
    
elif num1==num2==num3:
    print("All numbers are same: ",num1)
    
else:
    print("grater number is: ",num2)