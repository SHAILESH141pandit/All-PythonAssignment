# 2. Write a Python script to create a list of first N odd natural numbers.
emptylist = []
[emptylist.append(i) for i in range(1,1+int(input("Enter a number:  "))) if i%2!=0]
print("List of first N odd natural numbers is ",emptylist)