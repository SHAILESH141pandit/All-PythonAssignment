#2. Write a python script to calculate sum of squares of first N natural numbers.
qsum =0
for i in range(int(input("Enter a number: "))):
    qsum=qsum+((i+1)**2)
print("Sum of squares of first N natural numbers is",qsum)
