# 1. Use iter and next method to access all the elements of a given set using while loop.

# define set variable.
mySet = (1,2,3,4,5)

# use of iter method
it = iter(mySet)

# driver code
while True:
    # use of next method
    print(next(it))