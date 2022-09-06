# 8. Write a python program to multiply all the numbers in a list.
def List_Mult(*Lis):
    i = Lis[0]
    multi = 1
    for j in i:
        multi = multi * j
    return multi

    
myList = [1,2,3,4]
Result = List_Mult(myList)
print("multiple of numbers in  list is equal to ",Result)
