# 5. Write a recursive python function to calculate sum of cubes of first N natural numbers.

from numInput import numInput

# define function.
def cube_n(c):
    if c==1:
        return 1
    else:
        n = (c**3) + cube_n(c-1)
        return n

# call numInput function.
d = numInput()

# calling cube_n.
print(cube_n(d))