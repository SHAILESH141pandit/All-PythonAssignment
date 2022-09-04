# 5. Write a python program to check if all items in the tuple are the same.
my_tuple = ('abc', 'abc', 'abc')

x = all(i==my_tuple[0] for i in my_tuple)
if x == True:
    print("All items in the tuple are the same")
else:
    print("All items in the tuple are not same")