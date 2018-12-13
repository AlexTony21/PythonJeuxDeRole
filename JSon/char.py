import json
from random import randint
import os
from jet_de_de import jet_libre


class Character:
    def __init__(self, name):
        with open(name + '.json', 'r') as f:
            cont = f.read()
            cont = json.loads(cont)
            cont = cont[name]
            self.Name = cont['Name']
            self.Dexterity = cont["Dexterity"]
            self.Strength = cont["Strength"]
            self.Magic = cont["Magic"]
            self.Name = cont["Name"]
            self.MagicPoints = cont["MagicPoints"]
            self.Level = cont["Level"]
            self.Armor = cont["Armor"]
            self.Weapon = cont["Weapon"]
            self.LifePoints = cont["LifePoints"]
            self.Mental = cont["Mental"]
            self.Charisma = cont["Charisma"]
            self.Race = cont["Race"]
            self.Psychology = cont["Psychology"]
            self.Social = cont["Social"]
            self.Luck = cont["Luck"]
            self.Class = cont["Class"]
            self.Knowledge = cont["Knowledge"]
            self.Physical = cont["Physical"]

    def jet_de_ph(self, nb_faces):
        jet_libre(nb_faces, self.Physical)

    def jet_de_s(self, nb_faces):
        jet_libre(nb_faces, self.Social)

    def jet_de_v(self, nb_faces):
        jet_libre(nb_faces, self.Magic)

    def jet_de_f(self, nb_faces):
        jet_libre(nb_faces, self.Strength)

    def jet_de_d(self, nb_faces):
        jet_libre(nb_faces, self.Dexterity)

    def jet_de_c(self, nb_faces):
        jet_libre(nb_faces, self.Charisma)

    def jet_de_ps(self, nb_faces):
        jet_libre(nb_faces, self.Psychology)

    def jet_de_sa(self, nb_faces):
        jet_libre(nb_faces, self.Knowledge)

    def jet_de_m(self, nb_faces):
        jet_libre(nb_faces, self.Mental)
