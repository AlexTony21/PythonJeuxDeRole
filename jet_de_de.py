# -*- coding: cp1252 -*-
import random

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
        print "Permet d'effectuer un jet de reussite au des sans avoir besoin d'utiliser les donnee d'un personnage"
        print "forme = 'jet_libre(nb_faces = 100, nb_reu = 50, bonus = 0, crit = 5)'"
        print "nb_faces : nombre de faces du de, int positif"
        print "nb_reu : valeur de reussite avant prise en compte des modificateurs, int positif, inferieur à nb_faces"
        print "bonus : valeur retire au jet de de, int positif ou negatif"
        print "crit : taille de la plage critique(zone au plus bas et au plus haut de la taille renseigner), int positif"

def jet_brut(nb_faces, bonus = 0) :
        res = random.randint(1, nb_faces)
        res += bonus
        return res
