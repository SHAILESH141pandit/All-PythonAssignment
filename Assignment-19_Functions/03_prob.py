# 3. Write a python program to create a function which expects an unknown number of arguments.

def f(*t):
    print(t)
    # for i in t:
    #     print(i)
f(10)
f(10,20)
f(10,20,30)
f(10,20,30,40,50)