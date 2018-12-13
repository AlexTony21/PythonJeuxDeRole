import random
from random import randint
import sys
de = int(input("entrez valeur max du de: "))

rantier = randint(1,de)
ranobj  = randint(1,4)
i = 1

dif = int(input("entrez la valeur necessaire pour le drop: "))

def aleaobjet(rantier, ranobj, dif):

    if rantier > dif:
        print "Tier 1"
        if ranobj == 1:
            obj = "objet 1"
            return obj
        elif ranobj == 2:
            obj = "objet 2"
            return obj
        elif ranobj == 3:
            obj = "objet 3"
            return obj
        elif ranobj == 4:
            obj = "objet 4"
            return obj

print(aleaobjet(rantier,ranobj,dif))
raw_input('Press enter to quit...')
sys.exit('')