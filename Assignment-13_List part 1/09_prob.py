# 9. Write a Python script to create a list of city names taken from the user.

n = int(input("How many number of city name enter:  "))
mylist = []
for i in range(n):
    userip = input("Enter a City name:  ")
    mylist.append(userip)
print("List of city: ",mylist)