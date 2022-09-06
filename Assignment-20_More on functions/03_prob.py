''' 3. Write a python program to create a function that prints the even numbers from a given list.
    Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
'''
def EvenNum(*t):
    myList = t[0]
    for i in myList:
        if i%2==0:
            print(i,end=" ")

Sample_List = [1, 2, 3, 4, 5, 6, 7, 8, 9]
EvenNum(Sample_List)