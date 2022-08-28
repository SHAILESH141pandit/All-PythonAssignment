''' 10. Write a Python script to create a list, where each element of the list is a digit of a
    given number.'''

useri = input("Enter a number:  ")
emptylist = []
for i in useri:
    emptylist.append(int(i))
print(emptylist)