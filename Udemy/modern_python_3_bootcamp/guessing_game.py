from random import randint

guess_low = 1
guess_high = 10

actual_num = randint(guess_low, guess_high)

while True:

    print(f"Guess a number between {guess_low} and {guess_high}: ")
    try: 
        user = int(input())
    except TypeError:
        print("Please enter a valid number!")
    if user < guess_low or user > guess_high:
        raise ValueError("You entered a number outside of the range!")

    if user == actual_num:
        print("You guessed it! You won!")
        break
    elif user < actual_num:
        print("Too low, try again!")
    else:
        print("Too high, try again!")

    repeat = input("Do you want to guess again? (y/n)")
    if repeat.lower() == 'n':
        break
