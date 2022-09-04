# 7. Write a python program to copy elements 4 and 5 from the following tuple into a new.

tuple1=(1,2,3,4,5,6)
new_list = [] # empty list variavle.
for i in tuple1:
    if i==4 or i==5:
        new_list.append(i)
print("Resultant tuple is",tuple(new_list))