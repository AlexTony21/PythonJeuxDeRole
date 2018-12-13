# -*- coding: cp1252 -*-
import random
import sys
import glob
import json

def jet_libre(nb_faces = 100, nb_reu = 50, bonus = 0, crit = 5) :
        res = random.randint(1, nb_faces)
        if (res < crit) :
                print("reussite critique avec un jet de %s" % res)
                return

        if (res > nb_faces - crit) :
                print("echec critique avec un jet de %s" % res)
                return

        res -= bonus
        if (res < nb_reu):
                print("reussite avec un jet de %s" % res)
                return

        else :
                print("echec avec un jet de %s" % res)
                return


def jet_libre_help() :
        print ("Permet d'effectuer un jet de reussite au des sans avoir besoin d'utiliser les donnee d'un personnage")
        print ("forme = 'jet_libre(nb_faces = 100, nb_reu = 50, bonus = 0, crit = 5)'")
        print ("nb_faces : nombre de faces du de, int positif")
        print ("nb_reu : valeur de reussite avant prise en compte des modificateurs, int positif, inferieur à nb_faces")
        print ("bonus : valeur retire au jet de de, int positif ou negatif")
        print ("crit : taille de la plage critique(zone au plus bas et au plus haut de la taille renseigner), int positif")

def jet_brut(nb_faces=100, bonus = 0) :
        res = random.randint(1, nb_faces)
        res += bonus
        print(res)
        return res


def jet_specialise():
        while("Quel personnage souhaite agir?"):
            print(glob.glob("*.json"))
            choice = raw_input("Nom du personnage: ")
            print("Quel sera la caracteristique utilisee?")
            print("1.Physique 2.Social 3.Mental")
            print("4.Force 5.Dexterite 6.Charisme")
            print("7.Psychologie 8.Magie 9.Savoir")
            carac = input("Votre caracteristique: ")
            faces = input("Combien de faces possede votre de?")
            dice = random.randint(1, faces)
            with open('{0}.json'.format(choice), "r") as f:
                file = json.load(f)
                file = file[choice]
                print(dice)

            if carac == 1:
                jet = int(file["Physical"])
                if dice > jet:
                    print ("Action ratee")
                elif dice < jet:
                    print ("Action reussie")
                break
            elif carac == 2:
                jet = int(file["Social"])
                if dice > jet:
                    print ("Action ratee")
                elif dice < jet:
                    print ("Action reussie")
                break
            elif carac == 3:
                jet = int(file["Mental"])
                if dice > jet:
                    print ("Action ratee")
                elif dice < jet:
                    print ("Action reussie")
                break
            elif carac == 4:
                jet = int(file["Strength"])
                if dice > jet:
                    print ("Action ratee")
                elif dice < jet:
                    print ("Action reussie")
                break
            elif carac == 5:
                jet = int(file["Dexterity"])
                if dice > jet:
                    print ("Action ratee")
                elif dice < jet:
                    print ("Action reussie")
                break
            elif carac == 6:
                jet = int(file["Charisma"])
                if dice >= jet:
                    print ("Action ratee")
                elif dice < jet:
                    print ("Action reussie")
                break
            elif carac == 7:
                jet = int(file["Psychology"])
                if dice > jet:
                    print ("Action ratee")
                elif dice < jet:
                    print ("Action reussie")
                break
            elif carac == 8:
                jet = int(file["Magic"])
                if dice > jet:
                    print ("Action ratee")
                elif dice < jet:
                    print ("Action reussie")
                break
            elif carac == 9:
                jet = int(file["Knowledge"])
                if dice > jet:
                    print ("Action ratee")
                elif dice < jet:
                    print ("Action reussie")
                break



while("Quel type de lancer voulez vous effectuer?"):
    n = int(input("1.Libre 2.Brut 3.Specialise     "))
    if n == 1:
        jet_libre()
        break
    elif n == 2:
        jet_brut()
        break
    elif n == 3:
        jet_specialise()
        break

raw_input('Press enter to quit...')
sys.exit('')