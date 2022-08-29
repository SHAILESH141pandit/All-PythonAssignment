# 7. Write a Python script to remove all non int values from a list.
myList = [10,10.5,20,20.5,30,30.5,40.0,50.567]
emptylist = []
[emptylist.append(i) for i in myList if type(i)==int]
print(emptylist)