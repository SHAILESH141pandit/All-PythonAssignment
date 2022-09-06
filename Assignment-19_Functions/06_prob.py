# 6. Write a python program to create a function that finds a maximum of four numbers.
def numfun(*data):
    MaxNum = max(data)
    print(MaxNum)

numfun(1,20,10,15,100)