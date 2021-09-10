def nxt_qes():
    print("Next Question!!")


print('Hi , Welcome to our Quize')

inp = input('are you want to play! ')

if inp == "yes" or inp == "y":
    res = 1
else:
    print('Bye have a nice day!')
    quit()
rest = 0

if res == 1:
    print('your game is starting now , please check your answer first and use all small case')
    fst_ques = input('What is stand for www ? ')
    if fst_ques == 'world wide web':
        rest += 1

    nxt_qes()

    sec_ques = input('What is stand for ip ? ')
    if sec_ques == 'internet protocol':
        rest += 1

    print('Thanks for playing the game , Your score is ', rest)
    print('Bye have a nice day!')
    quit()
