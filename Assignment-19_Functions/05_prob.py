# 5. Write a python program to create a function which expects a list as an argument.
def list_fun(*myList):
    print(myList)
    print(type(myList))

myList = [1,2,3,4,5,'Hello','Python',20+10j]
list_fun(myList)