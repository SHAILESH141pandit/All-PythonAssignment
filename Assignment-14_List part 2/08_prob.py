''' 8. Write a Python script to print distinct elements along with their frequencies of
    occurrence in the list.
'''
mylist = [eval(i) for i in input("Enter list elements:  ").split(',')]
print("Enter a number to search in list",mylist)
elem = int(input(":  "))
count = 0
for i in range(len(mylist)):
    if elem == mylist[i]:
        count+=1
print("Not found in list" if count==0 else "Has frequency as",count,"in given list")