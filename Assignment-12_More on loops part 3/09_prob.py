# 9. Write a python script to calculate LCM of two numbers.
print("Enter two number.")
num1, num2 = int(input(":  ")), int(input(":  ")) 
if num1 > num2:  
    greater = num1  
else:  
    greater = num2  
while True: 
    if((greater % num1 == 0) and (greater % num2 == 0)):  
        lcm = greater  
        print("The L.C.M. of", num1,"and", num2,"is",lcm)
        break  
    greater+=1