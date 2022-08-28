# 7. Write a python script to print first N even natural numbers in reverse order.
z = int(input("Enter a number:  "))
i=0
while i<z:
    if i%2==0:
        print(z-i)
    i+=1