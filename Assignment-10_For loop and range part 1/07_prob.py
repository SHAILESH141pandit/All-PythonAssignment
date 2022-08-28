# 7. Write a python script to print first N even natural numbers in reverse order.
for i in range(int(input("Enter a number:  ")),0,-1):
    if i%2==0:
        print(i)