# 1.Write a python script to display the number of days in a given month number.
Mnum = int(input("Enter a month number:  "))
match Mnum:
    case 1:
        print("Number of days in january is 31 days.")
    case 2:
        print("Number of days in january is 28 / 29 days.")
    case 3:
        print("Number of days in january is 31 days.")
    case 4:
        print("Number of days in january is 30 days.")
    case 5:
        print("Number of days in january is 31 days.")
    case 6:
        print("Number of days in january is 30 days.")
    case 7:
        print("Number of days in january is 31 days.")
    case 8:
        print("Number of days in january is 31 days.")
    case 9:
        print("Number of days in january is 30 days.")
    case 10:
        print("Number of days in january is 31 days.")
    case 11:
        print("Number of days in january is 31 days.")
    case 12:
        print("Number of days in january is 31 days.")
    case _:
        print("Invalid input.")
