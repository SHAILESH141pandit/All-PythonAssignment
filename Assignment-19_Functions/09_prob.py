# 9. Write a python program to create a function to check whether a number falls in a given range.
def test_range(n):
    print(" %d is in the range."%int(n) if n in range(3,9) else "The number {} is outside the given range.".format(n))

test_range(7) # Yes!
test_range(15) # No!