# 4. Write a python program to create a function which expects kwargs arguments.
def fun(Name,**data):
    print(Name)
    for i,j in data.items():
        print(i,j)

fun('Shailesh', age=20, Gender='male', mob=12345)