# print("Hello world!")
import random

# this generates a random number from 0 to 100
number_to_be_guessed = random.randint(1, 100)
guess = int(input("Guess a number between 1 and 100: "))
number_of_guesses = 0

while number_of_guesses < 2:
    if guess == number_to_be_guessed:
        print("you got it right")
        break

    else:
        guess = int(input("Guess a number between 1 and 100: "))
    number_of_guesses += 1
if number_of_guesses == 2:
    print("Try again later, it's unfortunate you could not guess", number_to_be_guessed)

number_of_guesses += 1
