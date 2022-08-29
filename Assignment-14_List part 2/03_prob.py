# 3. Write a Python script to create a list of first N even natural numbers.
emptylist = []
num = int(input("Enter a number:  "))
[emptylist.append(i) for i in range(1,1+num) if i%2==0]
print("List of first",num,"even natural numbers is ",emptylist)