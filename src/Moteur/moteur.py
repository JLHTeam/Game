import sys
from case import *
from map import *
from element import *

class Moteur:
    def __init__(self, fileNameMap, modeGame):
        self.maps = Carte(fileNameMap)
        self.bombeList = []
        self.players = []
        self.players.append(JoueurH())

        if modeGame == "PvP":
            self.players.append(JoueurH())
        if modeGame == "PvE":
            self.players.append(JoueurIA())



def testMoteur():
    game = Moteur('', 1)
    pass


if __name__=='__main__':
    testMoteur()