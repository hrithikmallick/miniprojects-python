from sys import path


def add():
    name = input('Enter field name: ')
    userid = input('Enter user id: ')
    passwd = input('Enter password: ')
    with open('password.txt', 'a') as f:
        f.write(name + ' | ' + userid + ' | ' + passwd + "\n")


def view():
    print('\nName | Userid | Password')
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            print(line)


pwm = input('please enter master password ? ')

while True:
    opt = input(
        'To add a passsword use "add" and to view old password use "view" q to exit: ').lower()
    if opt == 'q':
        break
    if opt == 'add':
        add()
    elif opt == 'view':
        view()
    else:
        continue
