# 9. Write a python script to print binary equivalent of a given decimal number. (do not use bin() metho.
num = int(input("Enter a number:  "))
result = ''
while num != 0:
    result = result + str(num%2)
    num = num//2
for i in range(len(result)-1,-1,-1):
    print(result[i],end='')