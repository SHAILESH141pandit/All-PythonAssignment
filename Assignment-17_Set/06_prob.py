''' 6. Write a python program to add elements of list to a set thisset = {"Python", "Django", "JavaScript"}
mylist = ["Java", "C"]
'''
thisset = {"Python", "Django", "JavaScript"}
mylist = ["Java", "C"]
for i in mylist:
    thisset.add(i)
print("Updated Set is",thisset)