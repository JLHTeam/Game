import sys
from PyQt5.QtCore import *

class Element:
    def __init__(self, position = [1,1]):
        self.position = position



class Bombe(Element):
    """  """
    def __init__(self, sorte, position):
        super().__init__(position)
        self.sorte = sorte
        self.statut = 0 #0 = desactivé - 1 = waiting - 2 = expolse
        self.timer = QElapsedTimer()

        if self.sorte == 'Dynamite':
            self.power = 50 #Puissance de l'explosion
            self.TBE = 2000  #Time before explosion (ms)
            self.porte = 1

        if self.sorte == 'TNT':
            self.power = 100 #Puissance de l'explosion
            self.TBE = 2000  #Time before explosion (ms)
            self.porte = 2

        if self.sorte == 'BombeH':
            self.power = 200 #Puissance de l'explosion
            self.TBE = 3000  #Time before explosion (ms)
            self.porte = 4

    def refresh(self):
        if self.statut == 2:
            self.statut = 0
        elif self.statut == 1:
            if (self.timer.elapsed() > self.TBE):
                self.explose()
        return self.statut

    def activateBombe(self, positionJ):
        self.statut = 1
        self.position = positionJ
        self.timer.start()

    def explose(self):
        self.statut = 2
        print("explosion")



class Joueur(Element):
    def __init__(self, position, sorte):
        super().__init__(position)
        self.lastPosition = position.copy()
        self.sorte = sorte
        self.health = 300
        self.statut = 1

    def hurt(self, degat):
        self.health = max(self.health - degat, 0)
        if self.health == 0:
            self.statut = 0

    def refresh(self):
        pass

    def setAction(self): # récupérer action
        pass

    def creerBombe(self):
        self.commande = 0
        return 0

    def moveOK(self):
        self.lastPosition = self.position.copy()

    def moveBack(self):
        self.position = self.lastPosition.copy()

    def move(self, commande):
        if commande == 1:
            self.position[0] -= 1
        if commande == 2:
            self.position[0] += 1
        if commande == 3:
            self.position[1] -= 1
        if commande == 4:
            self.position[1] += 1
        self.commande = 0
        return -1


class JoueurIA(Joueur):
    def __init__(self):
        super().__init__()

    def refresh(self):
        pass


class JoueurH(Joueur):
    def __init__(self, position, sorte = 1):
        super().__init__(position, sorte)
        self.commande = 0
        self.sorte = sorte

    def refresh(self): # Evolution temps discret (Timer) du mouvement
        if self.commande == 5:
            return self.creerBombe()
        else:
            return self.move(self.commande)

    def setAction(self, commande): # Evolution temps réel de commande - buffer commande
        self.commande = commande


def testElement():
    elem = Element((0,0))
    bbmb = Bombe('TNT',(0,0))
    print(bbmb.power)

if __name__=='__main__':
    testElement()


