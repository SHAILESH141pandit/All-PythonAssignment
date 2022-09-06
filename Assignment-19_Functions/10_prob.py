# 10. Write a python program to create a function to check whether a given number is even or odd.
def oddeven(num):
    Result = ("{} is even number.".format(num) if num%2==0 else "%d is odd number."%int(num))
    return Result

print(oddeven(10))
print(oddeven(11))