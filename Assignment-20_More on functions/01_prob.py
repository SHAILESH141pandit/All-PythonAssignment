# 1. Write a python program to create a function that takes a list and returns a new list with the original lists unique elements.

def f1(*t):
    mylist = t[0]
    return set(mylist)

myList = [100,2,30,4,'Hello',45]
Result = f1(myList)
print("New List is ",list(Result))