# 11. Write a python script to take the month value in numeric format and display the number of days in it.
Mnum = int(input("Enter month in number:  "))

if Mnum==1 or Mnum==3 or Mnum==5 or Mnum==7 or Mnum==8 or Mnum==10 or Mnum ==12:
    print("month in is equal to 31 days")
elif Mnum==4 or Mnum==6 or Mnum==9 or Mnum==11:
    print("month in is equal to 30 days")
elif Mnum==2:
    print("month in is equal to 28 / 29 days")