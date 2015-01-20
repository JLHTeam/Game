import sys
##from PyQt4.QtCore import *
##from PyQt4.QtGui import *
##from PyQt4 import QtCore, QtGui
#http://openclassrooms.com/forum/sujet/pyqt-evenements-clavier-81893


class Joueur:
    def __init__(self):
        self.gauche = 1
        self.droite = 2
        self.haut = 3
        self.bas = 4
        self.positionX = 1
        self.positionY = 1
        self.vie = 3

    def next(self):
        # interaction appelle next()
        if commande = 'espace':
            self.creerBombe()
        else: # comment convertir la touche en un char
            self.move(direction)
        

    def setAction(self,commande): # récupérer action
        # dans le .g    class ActionWidget          def goLeft(self):   self.controller.goLeft()
        # dans le .c    class Controller            J = Joueur()
        # def goLeft(self): I = Interaction() ou M = Moteur()  timer() puis J.setAction à chaque time
        #
        self.commande=commande



    def creerBombe(self):
         pass

    def move(self,direction):
        if direction == 'gauche'
            self.positionX -= 1
        if direction == 'droite':
            self.positionX += 1
        if direction == 'bas':
            self.positionY -= 1
        if direction == 'haut':
            self.positionY += 1


class JoueurOrdi(Joueur):
    def __init__(self):
        super().__init__()

    def next(self):
        pass


def main():
    avatar = Avatar()
    for i in range(5):
        avatar.deplacer()
        print("positionX = " + str(avatar.positionX) + ", positionY = " + str(avatar.positionY))

    end
    #for i in range(5):
    #    avatar.deplacer()
    #    print("positionX = " + avatar.positionX + "positionY = " + avatar.positionY)
    # end

if __name__ == '__main__':
    main()

