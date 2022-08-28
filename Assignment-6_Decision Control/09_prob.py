# 9. Write a python script to check whether a given year is a leap year or not.

Gyear = int(input("Enter year: "))

# Aproch 1
Result = "Leap year" if Gyear%400==0 or (Gyear%4==0 and Gyear%100!=0) else "Non Leap year"
print(Result)

# Aproch 2
# if Gyear%400==0:
#     print("Leap year")

# else:
#     if Gyear%4==0 and Gyear%100!=0:
#         print("Leap year")

#     else:
#         print("Non Leap year")

# if Gyear%400==0 or (Gyear%4==0 and Gyear%100!=0):
#     print("Leap year")

# else:
#     print("Non Leap year")
