# 9. Write a recursive python function to print octal of a given decimal number.


# define function.
def decimal_TO_octal(n):
    if n > 1:
        decimal_TO_octal(n//8)
    print(n % 8, end='')


numInput = int(input("Enter a decimal number:   "))
# calling decimal_TO_octal.
decimal_TO_octal(numInput)
