import sys
from case import *
import csv

class Carte:
    """                   """
    def __init__(self, fileNameMap):
        self.matrice = None
        self.dim = (0,0)
        self.fileNameMap = fileNameMap

    def loadMap(self):
        fileMap = open(self.fileNameMap, 'r')
        data = csv.reader(fileMap, delimiter = '\t')
        self.matrice = [row for row in data]
        self.dim = (len(self.matrice), len(self.matrice[0])) # dimension de la matrice !!!

        # Creation de la matrice de Case (= Mur D / ND et Vide )
        for i,line in enumerate(self.matrice):
            for j,element in enumerate(line):
                self.matrice[i][j] = Case(int(element))

    def refresh(self):
        for i,line in enumerate(self.matrice):
            for j,element in enumerate(line):
                if element.health == 0:
                    self.matrice[i][j].sorte = 0





def testCarte():
    _carte = Carte('../Maps/map1.map')
    _carte.loadMap()
    _carte.refresh()


if __name__=='__main__':
    testCarte()




