import sys
from case import *
from map import *
from element import *
from random import *

class Moteur:
    def __init__(self, fileNameMap, modeGame, listeBombe):
        self.maps = Carte(fileNameMap)
        self.maps.loadMap()
        self.bombeList = []
        self.playerList = []

        for typeBombe in listeBombe:
            self.bombeList.append(Bombe(typeBombe))

        self.playerList.append(JoueurH([1,1]))
        if modeGame == "PvP":
            self.playerList.append(JoueurH(self.randPos()))
        if modeGame == "PvE":
            self.playerList.append(JoueurIA(self.randPos()))

    def setAction(self, commande, numPlayer):
        self.playerList[numPlayer].setAction(commande)

    def checkMove(self, player):
        if  self.maps.matrice[player.position[0]][player.position[1]].sorte != 0:
            return -1
        else:
            return 0

    def randPos(self):
        x = choice(range(self.maps.dim[0]))
        y = choice(range(self.maps.dim[1]))
        while self.maps.matrice[x][y].sorte != 0:
            x = choice(range(self.maps.dim[0]))
            y = choice(range(self.maps.dim[1]))
        return [x,y]

    def checkDegat(self, bombe):
        for player in self.playerList:
            if abs(player.position[0] - bombe.position[0]) <= bombe.porte:
                player.hurt(bombe.power)
            if abs(player.position[1] - bombe.position[1]) <= bombe.porte:
                player.hurt(bombe.power)

        affectedCaseList = list(range(-int(bombe.porte), bombe.porte))

        for i in affectedCaseList:
            if bombe.position[0] + i >= 0 and bombe.position[0] + i <= self.maps.dim[0]:
                self.maps.matrice[bombe.position[0]+i][bombe.position[1]].hurt(bombe.power)

        for i in affectedCaseList:
            if bombe.position[1] + i >= 0 and bombe.position[1] + i <= self.maps.dim[1]:
                self.maps.matrice[bombe.position[0]][bombe.position[1]+i].hurt(bombe.power)

    def refresh(self):
        self._activation = 0
        self._explosion = 0
        for i,player in enumerate(self.playerList):
            if player.refresh() == 0:
                self.bombeList[i].activateBombe(player.position)
                self._activation = 1 # Pour le son et image ACTIVATION BOMBE
            if player.refresh() == -1:
                if self.checkMove(player) == 0:
                    player.moveOK()
                else:
                    player.moveBack()
            #print(self.playerList[0].position)
            #print(self.playerList[1].position)

        for bombe in self.bombeList:
            if bombe.refresh() == 2:
                self.checkDegat(bombe)
                self._explosion = 1 # Pour le son et image EXPLOSION BOMBE

        self.maps.refresh()



def testMoteur():
    game = Moteur('../Maps/map1.map', "PvE")
    print(game.playerList[0].position)
    game.refresh()
    game.setAction(1,0)
    print('move')
    print(game.playerList[0].position)
    print('refresh')
    game.refresh()
    print(game.playerList[0].position)
    game.setAction(5,0) # Pose de la bombe
    print('Pose de la bombe')
    while 1:
        game.refresh()

if __name__=='__main__':
    testMoteur()