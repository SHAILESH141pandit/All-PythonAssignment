# 2. Write a python program to create a function that takes a number as a parameter and checks if the number is prime or not.

def primeORnot(num):
    for i in range(2,num):
        # Result = ("Number {} is not prime".format(num) if num%i==0 else "Number {} is not prime".format(num))
        if num%i==0:
            return "Number {} is not prime".format(num) 
    else:
        return "Number {} is prime".format(num)


num = int(input("Enter a number:  "))
print(primeORnot(num))