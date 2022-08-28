''' 1. Write a python script to remove the last digit from a given number. (for example, if
    user enters 2534 then your output should be 253)
'''

print("Enter a number.")
myStr = input(":  ")
length = len(myStr)
for i in range(length-1):
    print(int(myStr[i]),end="")