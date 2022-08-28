# 10. Write a python script to print the octal equivalent of a given decimal number. (do not use oct() method).
number = int(input("Enter a number:  "))
result = ''
while number != 0:
    result = result + str(number%8)
    number = number//8
for i in range(len(result)-1,-1,-1):
    print(result[i],end='')