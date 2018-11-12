import glob
import os

clear = lambda: os.system('cls')

clear()
print(glob.glob("*.txt"))
print "Which file do you want to read ?"
choice = raw_input("Name of the file : ")
clear()
file = open("" + choice + ".txt", "r")
print file.read()
raw_input('Press enter to quit...')
