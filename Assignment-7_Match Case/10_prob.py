'''10. Write a program to display day name on the basis of user's liking of a colour. Ask
user for his favorite colour. User can answer in a sentence like “I like red colour”.
Assuming all colour name entered by user is in lowercase. Use match case to display
day name associated with the colour.
a. Yellow - Monday
b. Blue - Tuesday
c. Orange - Wednesday
d. White - Thursday
e. Black - Friday
f. Red - Saturday
g. All other colours - Sunday'''

Cday = input("""Enter a Colours...
a. Yellow - Monday
b. Blue - Tuesday
c. Orange - Wednesday
d. White - Thursday
e. Black - Friday
f. Red - Saturday
g. All other colours - Sunday
:   """).lower()

match "yellow" in Cday:
    case True:
        print("Monday")
    case False:
        match "blue" in Cday:
            case True:
                print("Tuesday")
            case False:
                match "orange" in Cday:
                    case True:
                        print("Wednesday")
                    case False:
                        match "white" in Cday:
                            case True:
                                print("Thursday")
                            case False:
                                match "black" in Cday:
                                    case True:
                                        print("Friday")
                                    case False:
                                        match "red" in Cday:
                                            case True:
                                                print("Saturday")
                                            case _:
                                                print("Sunday")