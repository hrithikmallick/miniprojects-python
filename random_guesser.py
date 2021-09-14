import random


start = input('Press any button to start the game ')
del start

top_range = input('Please enter your top range for guessing!! ')
if top_range.isdigit():
    top_range = int(top_range)
else:
    print('Please Enter a digit ')
    quit()
random_number = random.randint(0, top_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")


print('you got the answer in ', guesses, 'attempts')
