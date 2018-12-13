from random import randint  # permet le random
import json
import sys



user_name = raw_input('Give me the name of your character : ')
user_class = raw_input('Give me the class of your character : ')
user_level = input('Give me the level of your character : ')
user_race = raw_input('Give me the race of your character. Example : Human, Dwarf, etc... : ')
user_weapon = raw_input('Tell me what\'s the weapon your character is using : ')
user_armor = raw_input('What kind of armor ? (Example : Light, Medium, Heavy) : ')
user_strength = int(input('What\'s the value of your character\'s strength : '))
user_dexterity = int(input('What\'s the value of your character\'s dexterity : '))
user_charisma = int(input('What\'s the value of your character\'s charisma : '))
user_psychology = int(input('What\'s the value of your character\'s psychology : '))
user_knowledge = int(input('What\'s the value of your character\'s knowledge : '))
user_magic = int(input('What\'s the value of your character\'s magic : '))
user_luck = randint(1, 7)
user_lp = randint(1, 20)
user_mp = randint(1, 20)
user_physical = ((int(repr(user_strength)) + int(repr(user_dexterity))) *10) /2
user_social = ((int(repr(user_charisma)) + int(repr(user_psychology))) * 10) /2
user_mental = ((int(repr(user_knowledge)) + int(repr(user_magic))) * 10) /2


Characters = {}
PlayerC = {"Name": user_name, "Class": user_class, "Level": repr(user_level), "Race": user_race, "Weapon": user_weapon,
           "Armor": user_armor, "LifePoints": repr(user_lp), "MagicPoints": repr(user_mp),
           "Physical": repr(user_physical), "Strength": repr(user_strength), "Dexterity": repr(user_dexterity),
           "Social": repr(user_social), "Charisma": repr(user_charisma), "Psychology": repr(user_psychology),
           "Mental": repr(user_mental), "Knowledge": repr(user_knowledge), "Magic": repr(user_magic),
           "Luck": int(repr(user_luck)) * 10}
Characters[user_name] = PlayerC

print(json.dumps(Characters))

with open(user_name + '.json', 'w') as f:
    f.write(json.dumps(Characters, indent=4))

raw_input('Press enter to quit...')
sys.exit('')
