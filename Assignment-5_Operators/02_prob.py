''' 2. Write a python script to get the last digit from a given number. (for example, if user
    enters 2089 then your output should be 9)
'''
print("Enter a number.")
numstr = input(":  ")
numLength = len(numstr)
print("Last digit from a given number is",int(numstr[numLength-1]))