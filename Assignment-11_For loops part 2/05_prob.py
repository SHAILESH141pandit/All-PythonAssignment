# 5. Write a python script to calculate sum of first N even natural numbers.
esum = 0
for xx in range(1,int(input("Enter a number:  "))+1):
    if xx%2==0:
        esum+=xx
print("Sum of first N even natural numbers is",esum)
