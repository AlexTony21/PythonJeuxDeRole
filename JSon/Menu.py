import os
clear = lambda: os.system('cls')

loop = 1
while loop == 1:
    clear()
    print("Welcome to the program")
    print("Choose a number")
    print("1- Run Sheet Character Creator")
    print("2- Read Characters Sheets")
    print("3- Dice Roll")
    print("4- Reward Generator")
    while "What is your choice ?":
        n = int(input('Your choice : '))
        if n == 1:
            os.system('fichedeperso.py')
            break
        elif n == 2:
            os.system('ReadFiche.py')
            break
        elif n == 3:
            os.system('jet_de_de.py')
            break
        elif n == 4:
            os.system('Drop.py')
            break
    print("1- Return to menu")
    print("2- Quit")
    while "What is your choice ?":
        m = int(input('Your choice : '))
        if m == 1:
            loop = 1
            break
        elif m == 2:
            loop = 2
            break
    if loop == 2:
        break
input("Press enter to quit...")
