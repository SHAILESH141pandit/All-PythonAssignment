'''
10. Write a python script to display the current date and time. First create variables to
store date and time, then display date and time in proper format (like: 13-8-2022 and
9:00 PM)

'''

import datetime

now = datetime.datetime.now()
print ("Current date and time : ")

print (now.strftime("%Y-%m-%d %H:%M:%S %p"))
print (now.strftime("%d-%m-%Y %H:%M %p"))