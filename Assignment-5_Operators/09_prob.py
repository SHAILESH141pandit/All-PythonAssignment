# 9. Write a python script to use NOT IN operator to display the data not present in list.

my_List = [1,2,3,4,5,6,7,8]
A = 1000 # to check it present in my list or not
Display = A not in my_List
if Display:
    print("Data",A,"is not present in my list")
