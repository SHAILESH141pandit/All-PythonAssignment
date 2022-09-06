# 4. Write a python program to create a function that checks whether a passed string is palindrome or not.
def Str_palindrome(Mystr):
    if Mystr[::1]==Mystr[::-1]:
        return "Passed string is palindrome"
    else:
        return "Passed string is not palindrome"

print("Enter a String.")
myStr = input(':-  ')
print(Str_palindrome(myStr))