# 4. Write a python script to print all Prime numbers between two given numbers (both values inclusive)
print("Enter two number.")
num1, num2 = int(input(":  ")), int(input(":  "))
for i in range(num1,num2+1):
    count = 0
    for x in range(1,i+1):
        if i%x==0:
            count+=1
    if count==2:
        print(i,end=' ')