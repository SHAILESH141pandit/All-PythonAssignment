# 5. Write a recursive python function to print first N even natural numbers.
def even_numb(x):
    if x>0:
        even_numb(x-1)
        if x%2==0:
            print(x)
a = 12
even_numb(a)