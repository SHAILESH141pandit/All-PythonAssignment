# 6. Write a python program to create a function and print a list where the values are square of numbers between 1 and 30.
def sqrnumb():
    thisList=[]
    for i in range(1,31):
        thisList.append(i**2)
    return thisList

print(sqrnumb())