import random

user_win = 0
bot_win = 0
start = input("Enter to start the game: ")
del start
gusees = 0
game = ['rock', 'paper', 'scissers']
while True:
    gusees += 1
    user_inp = input('Type Rock/Paper/Scissers or Q to quit: ').lower()

    if user_inp == 'q':
        print('User win', user_win, 'time', 'Computer win',
              bot_win, 'time in ', gusees-1, ' attempts')
        quit()

    if user_inp not in game:
        continue

    random_number = random.randint(0, 2)
    if user_inp == 'rock' and game[random_number] == 'scissers':
        user_win += 1
        print('You win')
        print('user input is ', user_inp,
              'and computer input is', game[random_number])
    elif user_inp == 'paper' and game[random_number] == 'rock':
        user_win += 1
        print('You win')
        print('user input is ', user_inp,
              'and computer input is', game[random_number])
    elif user_inp == 'scissers' and game[random_number] == 'paper':
        user_win += 1
        print('You win')
        print('user input is', user_inp,
              'and computer input is ', game[random_number])
    elif user_inp == game[random_number]:
        print("it's a draw")
        print('user input is', user_inp,
              'and computer input is', game[random_number])
    else:
        bot_win += 1
        print('computer win')
        print('user input is ', user_inp,
              'and computer input is ', game[random_number])
