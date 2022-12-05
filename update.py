count = 0
number_of_guess = 0
user_input = int(input("guess a number from 1 and 100: "))
lucky_number = 50
while count <= 5:
    if user_input == lucky_number:
        print(f"Congratulations, you have passed the drill. The number is {50}")
        break

    elif user_input >= 51 <= 60:
        print("you are slightly above the number")
    elif user_input <= 30:
        print("sorry! you are farther below the number")
    elif user_input >= 31 <= 49:
        print("sorry! you're close to the number")
    elif user_input >= 61 <= 100:
        print("you are far above the number")
    else:
        print("u no sabi")
    count += 1
