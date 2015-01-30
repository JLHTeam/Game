import sys
from PyQt5.QtCore import *

FPS = 60

class Element:
    def __init__(self, position = [1,1]):
        self.position = position



class Bombe(Element):
    """  """
    def __init__(self, sorte, position):
        super().__init__(position)
        self.sorte = sorte
        self.statut = 0 #0 = desactivé - 1 = waiting - 2 = expolse

        if self.sorte == 'Dynamite':
            self.power = 50 #Puissance de l'explosion
            self.TBE = 2  #Time before explosion (s)
            self.porte = 1

        if self.sorte == 'TNT':
            self.power = 100 #Puissance de l'explosion
            self.TBE = 2  #Time before explosion (s)
            self.porte = 2

        if self.sorte == 'BombeH':
            self.power = 200 #Puissance de l'explosion
            self.TBE = 3  #Time before explosion (s)
            self.porte = 4

    def refresh(self): # Rafrachissement tout les 1/FPS
        if self.statut == 2:
            self.statut = 0
        elif self.statut == 1:
            self.clock += 1
            if self.clock > self.TBE*FPS:
                self.explose()
        return self.statut

    def activateBombe(self, positionJ):
        if self.statut == 0:
            self.statut = 1
            self.position = positionJ
            self.clock = 0

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
        if commande == "G":
            self.position[0] -= 1
        if commande == "D":
            self.position[0] += 1
        if commande == "B":
            self.position[1] -= 1
        if commande == "H":
            self.position[1] += 1
        self.commande = 0
        return -1


class JoueurIA(Joueur):
    def __init__(self, position, sorte = 1):
        super().__init__(position, sorte)
        self.posGoal = []
        self.posBombList = []
        self.sorte = sorte
        self.distanceView = 3

    def refresh(self): # Evolution temps discret (Timer) du mouvement
        pass

    def setAction(self): # Evolution temps réel de commande - buffer commande
        pass

    def setAttackGoal(self): # essaye de poser une bombe
        pass

    def setDefenseGoal(self): # fuire une bombe recherche d'un chemin !!!
        pass

    def setGoal(self):
        if self.isDangerousAreas():
            self.setAttackGoal()
        else:
            self.setDefenseGoal()

    def isDangerousAreas(self):
        for posBombe in self.posBombList:
            if abs(self.position[0] - posBombe[0]) <= self.distanceView or abs(self.position[1] - posBombe[1]) <= self.distanceView:
                return 1
            else:
                return 0

class JoueurH(Joueur):
    def __init__(self, position, sorte = 1):
        super().__init__(position, sorte)
        self.commande = 0
        self.sorte = sorte

    def refresh(self): # Evolution temps discret (Timer) du mouvement
        if self.commande == "BB":
            return self.creerBombe()
        else:
            return self.move(self.commande)

    def setAction(self, commande): # Evolution temps réel de commande - buffer commande
        self.commande = commande




def testElement():
    elem = JoueurIA([1,2])
    print(elem.health)

if __name__=='__main__':
    testElement()


