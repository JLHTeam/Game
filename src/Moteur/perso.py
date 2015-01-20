import sys
##from PyQt4.QtCore import *
##from PyQt4.QtGui import *
##from PyQt4 import QtCore, QtGui
#http://openclassrooms.com/forum/sujet/pyqt-evenements-clavier-81893


class Joueur:
    def __init__(self):
        self.gauche = 1
        self.droite = 2
        self.haut = None
        self.bas = None
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
        self.positionX=1
        self.positionY=1

    def deplacer(self):
        Joueur1 = Joueur()
        commande = Joueur1.commande()
        if commande== Joueur1.gauche:
            self.positionX -= 1
        if commande == Joueur1.droite:
            self.positionX += 1
        if commande == Joueur1.haut:
            self.positionY -= 1
        if commande == Joueur1.bas:
            self.positionY += 1

    def poserBombe(self):
        pass

def main():
    avatar = Avatar()
    avatar.deplacer()
    print(avatar.positionX)

if __name__ == '__main__':
    main()

