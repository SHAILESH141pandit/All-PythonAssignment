# 9. Write a python program to merge two python dictionaries into one dictionary.

# Creat two dect...
dict1 = {'A':1,'B':2}
dict2 = {'C':3,'D':4}
# Emty dict. object created.
Resultant_Dict = {}
# merge two dictionaries item into one dict.
for i in dict1:
    Resultant_Dict[i]=dict1[i]
for e in dict2:
    Resultant_Dict[e]=dict2[e]
print(Resultant_Dict)