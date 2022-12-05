import random

for roll in range(12):
    # January = 1
    # February = 2
    # March = 3
    # April = 4
    # May = 5
    # June = 6
    # July = 7
    # August = 8
    # September = 9
    # October = 10
    # November = 11
    # December = 12
    number = random.randrange(0, 13)
    if number == 1:
        print("January")
    elif number == 2:
        print("February")
    elif number == 3:
        print("March")
    elif number == 4:
        print("April")
    elif number == 5:
        print("May")
    elif number == 6:
        print("June")
    elif number == 7:
        print("July")
    elif number == 8:
        print("August")
    elif number == 9:
        print("September")
    elif number == 10:
        print("October")
    elif number == 11:
        print("November")
    elif number == 12:
        print("December")
