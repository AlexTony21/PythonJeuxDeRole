import glob
import os
import json
import sys
from pprint import pprint
clear = lambda: os.system('cls')

clear()
print(glob.glob("*.json"))
print("Which file do you want to read ?")

choice = raw_input("Name of the file : ")
clear()
with open('{0}.json'.format(choice), 'r') as f:
    file = json.load(f)
pprint(file)
raw_input('Press enter to quit...')
sys.exit('')
