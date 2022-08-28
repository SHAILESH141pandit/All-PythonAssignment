''' 8. Write a python script to check whether a given quadratic equation has two real &
distinct roots, real & equal roots or imaginary roots'''

print("General form of equation:- ax**2 + bx + c = 0")
a = int(input("Enter a (a is donot equql to zero):  "))
b = int(input("Enter b:  "))
c = int(input("Enter c:  "))
d = (b**2)-(4*a*c)
print()
if d>0:
    print("Type of Roots: Two real & distinct roots")
elif d==0:
    print("Type of Roots: Two real & equal roots")
else:
    print("Type of Roots: Two imaginary/Complex roots")