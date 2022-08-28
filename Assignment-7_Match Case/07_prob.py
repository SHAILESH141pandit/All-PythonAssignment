"""7. Write a python program to check whether a given number is positive, negative or
zero using match case statement.
"""

numb = int(input("Entera number:  "))
match numb>0:
    case True:
        print("Given number is positive.")
    case False:
        match numb<0:
            case True:
                print("Given number is negative.")
match numb==0:
    case True:
        print("Given number is zero.")