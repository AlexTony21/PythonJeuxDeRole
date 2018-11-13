import os

clear = lambda: os.system('cls')

loop = 1
while loop == 1:
    clear()
    print "Welcome to the program"
    print "Choose a number"
    print "1- Run Sheet Character Creator"
    print "2- Read Characters Sheets"
    while "What is your choice ?":
        n = input('Your choice : ')
        if n == 1:
            os.system("ficheperso.py 1")
            break
        elif n == 2:
            os.system("ReadFiche.py 1")
            break
    print "1- Return to menu"
    print "2- Quit"
    while "What is your choice ?":
        m = input('Your choice : ')
        if m == 1:
            loop = 1
            break
        elif m == 2:
            loop = 2
            break
    if loop == 2:
        break
raw_input("Press enter to quit...")
