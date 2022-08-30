'''3. Write a menu driven program with the following options:
    a. Check whether a given set of three numbers are lengths of an isosceles triangle or not
    b. Check whether a given set of three numbers are lengths of sides of a right angled triangle or not
    c. Check whether a given set of three numbers are equilateral triangle or not
    d. Exit.
'''


print("Enter sides of triangle:")
side1, side2, side3 = int(input(":  ")), int(input(":  ")), int(input(":  "))

print('''
Enter a :- for check an isosceles triangle or not.
Enter b :- for right angled triangle or not.
Enter c :- for check equilateral triangle or not.
Enter c :- for Exit.
''')
Userinp = input(":  ")

match Userinp:
    case "a":
        match side1 == side2 or side2 == side3 or side3 == side1:
            case True:
                print("The given Triangle is isosceles")
            case False:
                print("The given Triangle is not isosceles")

    case "b":
        match (side1**2)==(side2**2)+(side3**2) or (side2**2)==(side1**2)+(side3**2) or (side3**2)==(side1**2)+(side3**2):
            case True:
                print("The given Triangle is right angled.")
            case False:
                print("The given Triangle is not right angled.")

    case "c":
        match side1 == side2 and side2 == side3:
            case True:
                print("The Given Triangle is equilateral")
            case False:
                print("The Given Triangle is not equilateral")

    case "d":
        exit # exit