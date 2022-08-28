'''5. Write a program which takes a number from user. Print Saurabh Shukla if the number
is even, print Prateek Jain if the number is negative odd number and print Aditya
Choudhary if number is positive odd number.'''
num = int(input("Enter a number:  "))
match num%2==0:
    case True:
        print("Saurabh Shukla")

match num%2==0:
    case False:
        match num<0:
            case True:
                print("Prateek Jain")
                
match num%2==0:
    case False:
        match num>0:
            case True:
                print("Aditya Choudhary")
