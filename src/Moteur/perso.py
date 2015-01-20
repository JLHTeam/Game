import sys
##from PyQt4.QtCore import *
##from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui
#http://openclassrooms.com/forum/sujet/pyqt-evenements-clavier-81893


class Joueur:
    def __init__(self):
        self.g = 1
        self.d = 2
        self.h = None
        self.b = None
        #self.event = []
        super().__init__()

    def commande(self):
        direction = None
        direction = int(input())
        print(direction)
        #input() # normalement à mettre dans bombermanText
        #self.controller.bouger(direction)
        #self.actualiser()
        return(direction)

    def actualiser(self):
        pass

class Avatar:
    def __init__(self):
        super().__init__()
        self.posX=1
        self.posY=1

    def deplacer(self):
        Joueur1 = Joueur()
        print(Joueur1.commande())
        print(Joueur1.g)
        if Joueur1.commande() == Joueur1.g:
            self.posX -= 1
        if Joueur1.commande() == Joueur1.d:
            self.posX += 1
        if Joueur1.commande() == Joueur1.h:
            self.posY -= 1
        if Joueur1.commande() == Joueur1.b:
            self.posY += 1

    def poserBombe(self):
        pass

def main():
    avatar = Avatar()
    avatar.deplacer()
    print(avatar.posX)

if __name__ == '__main__':
    main()

