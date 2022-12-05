max = float("-inf")
min = float("+inf")
user_input = float(input("Enter number: "))
while user_input != 0:
    if user_input > max:
        max = user_input
    if user_input < min and user_input != 0:
        min = user_input
    user_input = float(input("Enter a number or 00 to quit: "))
print("max number is: ", max)
print("min number is: ", min)
