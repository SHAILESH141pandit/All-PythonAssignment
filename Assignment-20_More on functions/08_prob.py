''' 8. Write a python program to create a function that accepts a string and calculate the
number of upper case letters and lower case letters.'''
def Str_test(s):
    Upper_case = 0
    Lower_case = 0
    for i in s:
        if i.isupper():
            Upper_case+=1
        elif i.islower():
            Lower_case+=1
        else:
            pass
    print("No. of Upper case characters : ",Upper_case)
    print("No. of Lower case Characters : ",Lower_case)

s="AdBeCfd"
Str_test(s)