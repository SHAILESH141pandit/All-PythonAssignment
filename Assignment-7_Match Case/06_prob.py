''' 6. Write a python program to check whether a given string is a multiword string or single
    word string using match case statement.
'''
print("Enter a string to check is multiword string or single word string.")
myStr = input(":  ")

match " " in myStr:
    case True:
        match myStr==" ":
            case True:
                print("Yes single string")
            case False:
                print("Yes multiword string")
    case False:
        print("Yes single string")