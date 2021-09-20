from cryptography.fernet import Fernet

# only run at starting at program to generate the key
# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as f:
#         f.write(key)
# write_key()


def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key


def encryp(val):
    return fer.encrypt(val.encode()).decode()


def decryp(val):
    return fer.decrypt(val.encode()).decode()


def add():
    name = input('Enter field name: ')
    userid = input('Enter user id: ')
    passwd = input('Enter password: ')
    with open('password.txt', 'a') as f:
        f.write(encryp(name) + ' | ' + encryp(userid) +
                ' | ' + encryp(passwd) + "\n")
        # print(encryp(name))
        # print(decryp(encryp(name)))


def view():
    print('\nName | Userid | Password')
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            name, userid, password = data.split(' | ')
            print("Name: "+decryp(name)+" Userid: " +
                  decryp(userid)+" Password: "+decryp(password))


# load key from key file
# and generate key using
key = load_key()
fer = Fernet(key)

while True:
    opt = input(
        'To add a passsword use "add" and to view old password use "view" q to exit: ').lower()
    if opt == 'q':
        break
    if opt == 'add' or opt == 'a':
        add()
    elif opt == 'view' or opt == 'v':
        view()
    else:
        continue
