import sys
from case import *
from map import *
from

class Moteur:
    def __init__(self, fileNameMap, modeGame):
        self.maps = Carte(fileNameMap)
        self.bombeList = []
        self.players = []

        if modeGame == 0:
            pass
        if modeGame == 1:
            pass




def testMoteur():
    game = Moteur('')
    pass


if __name__=='__main__':
    testMoteur()