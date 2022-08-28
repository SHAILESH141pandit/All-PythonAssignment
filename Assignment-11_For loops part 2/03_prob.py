# 3. Write a python script to calculate sum of cubes of first N natural numbers.
num = int(input("Enter a number: "))
qsum=0
for i in range(num+1):
    qsum+=(i**3)
print("Sum of cubes of first N natural numbers is",qsum)