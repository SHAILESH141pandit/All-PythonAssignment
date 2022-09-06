# 9. Write a python program to create a function to check whether a string is a pangram or not.
def check_pangram(myStr):
  if len(set('abcdefghijklmnopqrstuvwxyz') - set(myStr.lower())) == 0 :
    return True
  return False

user_str = input("Enter a string to check for pangram : ")

if check_pangram(user_str):
  print("It is a pangram string")
else:
  print("Not a pangram string")
