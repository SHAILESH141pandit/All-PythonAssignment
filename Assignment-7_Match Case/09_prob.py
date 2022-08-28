'''9. Write a python script to check whether a given year is
a. Non century leap year
b. Century leap year
c. Non century non leap year
d. Century non leap year
'''
Years = int(input("Enter a year:  "))
match Years%100==0 and Years%400!=0:
    case True:
        print("Given year is Non century leap year")
    case False:
        print("Given year is Century leap year")
    case _:
        match Years%100!=0 and Years%400==0:
            case True:
                print("Given year is Non century not leap year")
            case False:
                print("Given year is century not leap year")