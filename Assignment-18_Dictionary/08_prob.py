# 8. Write a python program to convert two lists into a dictionary in a way that item from list1 is the key and item from list2 is the value.

# Define two list.
list1 = ['A','B','C']
list2 = [1,2,3]
# Emty dict object created.
Resultant_Dict = {}
# logic define.
for i in range(len(list1)):
    Resultant_Dict[list1[i]]=list2[i]
print(Resultant_Dict)
