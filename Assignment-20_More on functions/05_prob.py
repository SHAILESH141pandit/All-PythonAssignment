# 5. Write a python program to create a function to find the Min of three numbers.
def minValue():
    print("Enter three numbers.")
    num1, num2, num3 = int(input(":-  ")),  int(input(":-  ")), int(input(":-  ")) 
    if num1<num2 and num1< num3 :
        return num1
    elif num2<num3:
        return num2
    else:
        return num3
        
print("Minimum number is ",minValue())