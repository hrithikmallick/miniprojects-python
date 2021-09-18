import random

user_win = 0
bot_win = 0
start = input("Enter any key to start the game: ")
del start
gusees = 1
game = ['rock', 'paper', 'scissers']
while True:
    gusees += 1
    user_inp = input('Type Rock/Paper/Scissers or Q to quit: ').lower()

    if user_inp == 'q':
        print('Usere win', user_win, 'time', 'Computer win',
              bot_win, 'time ')
        quit()

    random_number = random.randint(0, 2)
    if user_inp == game[random_number]:
        user_win += 1
    else:
        bot_win += 1
