'''12. Write a python script to accept one complex number from the user and display the
greater number between real part and imaginary part.
'''
print("Enter a Complex number")
comp = complex(input(": "))


if comp.real>comp.imag:
    print("Real partis", comp.real)
    print("Imaginary partis", comp.imag)
    print("Real part is greater then Imaginary part.")

else:
    print("Real partis", comp.real)
    print("Imaginary partis", comp.imag)
    print("Imaginary part is greater then Real part.")

