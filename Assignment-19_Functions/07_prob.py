# 7. Write a python program to sum all the numbers in a list.
def List_sum(*Lis):
    i = Lis[0]
    print("Sum all the numbers in a list is equal to",sum(i))

myList = [1,2,3,4,5]
List_sum(myList)