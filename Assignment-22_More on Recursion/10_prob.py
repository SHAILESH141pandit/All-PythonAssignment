# 10. Write a recursive python function to find the Nth term of the Fibonacci series.

from numInput import numInput
# define function.
def Fibnachi_ser(n):
    if n <= 2:
      return n - 1
    else:
      return Fibnachi_ser(n - 1) + Fibnachi_ser(n - 2)

# call numInput function.
num = numInput()

# calling Fibnachi_ser function.
print(Fibnachi_ser(num))
