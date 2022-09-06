''' 10. Write a python script to add two numbers 25 (in octal) and 39 (in hexadecimal) and
    display the result in binary format.
'''
number1 = 25 
number2 = 39
# Number to octal conversion
number1 = oct(number1)
# octal to number conversion
bnum1 = int(number1, 8)


# Number to Hexadecimal conversion
number2 = hex(number2)
# Hexadecimal to number conversion
bnum2 = int(number2, 16)

print("The result in binary format is ",bin(bnum1 + bnum2))

print(bin(0o25)+bin(0x39))