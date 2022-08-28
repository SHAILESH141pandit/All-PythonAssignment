'''8. Write a python script to check whether two given strings are identical, first string
comes before the second in dictionary order or first string comes after the second
string in dictionary order using match case statement'''

F1str = input("Enter a first string:  ")
F2str = input("Enter a second string:  ")

match F1str==F2str:
    case True:
        print("given strings are identical.")
    case False:
        print("given strings are identical.")
