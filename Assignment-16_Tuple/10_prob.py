''' 10. Write a python program to change the first item (22) of a list within the following tuple
to 222. tuple1 = (11, [22, 33], 44, 55)'''

# Approach 01.
tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0]=222
print("Updated tuple is",tuple1)

# Approach 02.
# tuple1 = (11, [22, 33], 44, 55)
# my_list = list(tuple1)
# print(my_list)
# my_list[1][0]=222
# print("Updated tuple is",tuple(tuple1))