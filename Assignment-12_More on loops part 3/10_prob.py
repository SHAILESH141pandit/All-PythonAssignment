# 10. Write a python script to calculate HCF of two numbers.

print("Enter two number.")
num1, num2 = int(input(":  ")), int(input(":  "))
if num1>num2:
    s = num2
else:
    s = num1
for i in range(1,s+1):
    if num1%i==0 and num2%i==0:
        hcf = i
print("The H.C.F. of", num1,"and", num2,"is",hcf)  