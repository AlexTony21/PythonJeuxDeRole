import random
import json
from random import randint

#variable définissant le chiffre max du dé
de = int(input("entrez valeur max du de: "))

#lancer correspond au lancer du dé, Rantier correspond au type d'objet récupéré
#ranobj correspond à l'objet selectionner dans la liste json
lancer = randint(1,de)
rantier = str(randint(0,2))
ranobj  = randint(0,4)

#rolcap correspond au chiffre à atteindre pour récupéré l'objet
rolcap = int(input("entrez la valeur necessaire pour le drop: "))

def aleaobjet(lancer, ranobj, rantier, dif):

    with open("item.json","r") as f: #ouverture du json
                file = json.load(f)
                file = file[rantier] #séléction du type d'objet
    if lancer >= rolcap:
        obj = file[ranobj] #séléction de l'objet dans son type
        print ("Wow! you just found a "+obj)
    else:
        print "too bad! you found nothing!"

aleaobjet(lancer, ranobj, rantier, dif)
raw_input('Press enter to quit...')
sys.exit('')
