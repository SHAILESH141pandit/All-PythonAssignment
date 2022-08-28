''' 2. Write a menu driven program to perform following operations - Addition, Subtraction,
Multiplication, Division.
'''
print("Enter a first and second numbers.")
num1,num2=int(input(":  ")),int(input(":  "))
opr = input("Enter operations for +, -, *, / : ")

match opr:
    case '+':
        print("Addition of numbers is",num1+num2)
    case '-':
        print("Subtraction of numbers is",num1-num2)
    case '*':
        print("Multiplication of numbers is",num1*num2)
    case '/':
        print("Division of numbers is",num1/num2)
    case _:
        print("nvalied operation")