# -*- coding: cp1252 -*-
from random import randint #permet le random
import os
import mysql.connector #permet la connexion à la bdd

mydb = mysql.connector.connect(host="localhost", user="root", database="testp")
mycursor = mydb.cursor()

clear = lambda: os.system('cls')

#création des infos pour le perso
user_name = raw_input('Give me the name of your character : ')
clear()
user_class = raw_input('Give me the class of your character : ')
clear()
user_level = input('Give me the level of your character : ')
clear()
user_race = raw_input('Give me the race of your character. Example : Human, Dwarf, etc... : ')
clear()
user_weapon = raw_input('Tell me what\'s the weapon your character is using : ')
clear()
user_armor = raw_input('What kind of armor ? (Example : Light, Medium, Heavy) : ')
clear()
user_strength = input('What\'s the value of your character\'s strength : ')
clear()
user_dexterity = input('What\'s the value of your character\'s dexterity : ')
clear()
user_charisma = input('What\'s the value of your character\'s charisma : ')
clear()
user_psychology = input('What\'s the value of your character\'s psychology : ')
clear()
user_knowledge = input('What\'s the value of your character\'s knowledge : ')
clear()
user_magic = input('What\'s the value of your character\'s magic : ')
clear()
user_luck = randint(1,7)
user_lp = randint(1,20)
user_mp = randint(1,20)
user_physical = (user_strength + user_dexterity) / 2
user_social = (user_charisma + user_psychology) / 2
user_mental = (user_knowledge + user_magic) / 2

#création de la bdd
table_name = user_name.upper()
mycursor.execute("CREATE TABLE IF NOT EXISTS PERSOS2(Id INT AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(255), Class VARCHAR(255), Level INT NOT NULL, Race VARCHAR(255), Weapon VARCHAR(255), Armor VARCHAR(255), LifePoints INT NOT NULL, MagicPoints INT NOT NULL, Physical INT NOT NULL, Strength INT NOT NULL, Dexterity INT NOT NULL, Social INT NOT NULL, Charisma INT NOT NULL, Psychology INT NOT NULL, Mental INT NOT NULL, Knowledge INT NOT NULL, Magic INT NOT NULL, Luck INT NOT NULL)")

file = open("" + user_name + ".txt", "w")
print "-------------------------------------------"
print ""
print "Name : " + user_name
file.write("Name : " + user_name + "\n")
print "Class : " + user_class
file.write("Class : " + user_class + "\n")
print "Level : " + repr(user_level)
file.write("Level : " + repr(user_level) + "\n")
print "Race : " + user_race
file.write("Race : " + user_race + "\n")
print "Weapon : " + user_weapon
file.write("Weapon : " + user_weapon + "\n")
print "Armor : " + user_armor
file.write("Armor : " + user_armor + "\n")
print "Life Points : " + repr(user_lp)
file.write("Life Points : " + repr(user_lp) + "\n")
print "Magic Points : " + repr(user_mp)
file.write("Magic Points : " + repr(user_mp) + "\n")
Physical = 'Physical - ' + repr(user_physical) + '0% (Strength ' + repr(user_strength) + ', Dexterity ' + repr(user_dexterity) + ')'
Social = 'Social - ' + repr(user_social) + '0% (Charisma ' + repr(user_charisma) + ', Psychology ' + repr(user_psychology) + ')'
Mental = 'Mental - ' + repr(user_mental) + '0% (Knowledge ' + repr(user_knowledge) + ', Magic ' + repr(user_magic) + ')'
Luck = 'Luck - ' + repr(user_luck) + '0%'
print Physical
file.write(Physical + "\n")
print Social
file.write(Social + "\n")
print Mental
file.write(Mental + "\n")
print Luck
file.write(Luck + "\n")
print ""
file.close()
sql = "INSERT INTO PERSOS2(Name, Class, Level, Race, Weapon, Armor, LifePoints, MagicPoints, Physical, Strength, Dexterity, Social, Charisma, Psychology, Mental, Knowledge, Magic, Luck) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
val = ("" + user_name + "", "" + user_class + "", "" + repr(user_level) + "", "" + user_race + "", "" + user_weapon + "", "" + user_armor + "", "" + repr(user_lp) + "", "" + repr(user_mp) + "", "" + repr(user_physical) + "0", "" + repr(user_strength) + "", "" + repr(user_dexterity) + "", "" + repr(user_social) + "0", "" + repr(user_charisma) + "", "" + repr(user_psychology) + "", "" + repr(user_mental) + "0", "" + repr(user_knowledge) + "", "" + repr(user_magic) + "", "" + repr(user_luck) + "")
mycursor.execute(sql, val)

mydb.commit() #requis pour faire les changements

print('Data saved...')
print('Wanr to create another sheet ?')
n = raw_input('Y/N : ')
if n == 'Y':
    import ficheperso.py
elif n == 'y':
    import ficheperso.py
raw_input('Press enter to quit...')
