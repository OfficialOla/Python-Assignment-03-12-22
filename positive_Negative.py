user_input = int(input("enter a number or 0 to end: "))
positive_number = 0
negative_number = 0
number = 0
while user_input != 0:
    user_input = int(input("enter a number or 0 to end: "))
    if user_input >= 0:
        user_input += user_input
        positive_number += 1
    elif user_input < 0:
        # number += number
        negative_number += 1
    elif user_input == 0:
        print(positive_number)
total_number_of_input = positive_number + negative_number
total = number
average = total / total_number_of_input
print(total)
print(average)
print("The number of positives is ", positive_number)
print("The number of negatives is ", negative_number)
user_input += 1
