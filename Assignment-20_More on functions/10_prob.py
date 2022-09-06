# 10. Write a python program to create a function to check whether a string is an anagram or not.
def anagram_or_not(str1,str2):
    if len(set(str1) - set(str2)) == 0 :
        return True
    return False


user_str1 = input("Enter a first string: ").lower()
user_str2 = input("Enter a second string: ").lower()

if anagram_or_not(user_str1,user_str2):
  print("It is a anagram string")
else:
  print("Not a anagram string")
