'''4. Write a program which takes user's age and display the category of person.
    Age below 10 years- Kid,
    Age below 20 - Teen,
    Age below 40 - young,
    Age below 60 - Experienced,
    Age above or equal 60 - Senior Citizen.
'''

print("Enter Age.")
Age = int(input(":  "))
match 0<Age<10:
    case True:
        print("Category of person is","\"Kid\"")

match 10<=Age<20:
    case True:
        print("Category of person is","\"Teen\"")

match 20<=Age<40:
    case True:
        print("Category of person is","\"Young\"")

match 40<=Age<60:
    case True:
        print("Category of person is","\"Experienced\"")

match Age>=60:
    case True:
        print("Category of person is","\"Senior Citizen\"")


