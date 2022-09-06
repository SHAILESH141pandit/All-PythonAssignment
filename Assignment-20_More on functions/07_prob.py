# 7. Write a python program to access a function inside a function.
def A():
    def B():
        print("Hello")
    return B()
# function call.
A()