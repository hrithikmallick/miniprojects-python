import random

while True:
    rnNum = random.randint(1, 6)
    if rnNum == 1:
        print("----------")
        print("|        |")
        print("|    O   |")
        print("|        |")
        print("----------")
    if rnNum == 2:
        print("----------")
        print("|        |")
        print("| O    O |")
        print("|        |")
        print("----------")
    if rnNum == 3:
        print("----------")
        print("| O      |")
        print("|    O   |")
        print("|      O |")
        print("----------")
    if rnNum == 4:
        print("----------")
        print("| O    O |")
        print("|        |")
        print("| O    O |")
        print("----------")
    if rnNum == 5:
        print("----------")
        print("| O    O |")
        print("|    O   |")
        print("| O    O |")
        print("----------")
    if rnNum == 6:
        print("----------")
        print("| O    O |")
        print("| O    O |")
        print("| O    O |")
        print("----------")

    qt = input("Enter to Roll again and q to quit:")
    if qt == "q":
        break
    elif qt == "":
        continue
    else:
        print("!!!!!! Wrong input !!!!!!")
        break
