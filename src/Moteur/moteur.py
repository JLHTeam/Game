import sys
from case import *
from map import *
from element import *

class Moteur:
    def __init__(self, fileNameMap, modeGame):
        self.maps = Carte(fileNameMap)
        self.maps.loadMap()
        self.bombeList = []
        self.playerList = []
        self.playerList.append(JoueurH((1,1), 1))
        self.bombeList.append(Bombe('Dynamite', (0,0)))

        if modeGame == "PvP":
            self.playerList.append(JoueurH((1,1), 1))
        if modeGame == "PvE":
            self.playerList.append(JoueurIA((1,1), 1))



    def moveCommande(self, commande, numPlayer):
        self.playerList[numPlayer].setAction(commande)

    def checkMove(self, player):
        if  self.maps.matrice[player.position[0]][player.position[1]].sorte != 0:
            return -1
        else:
            return 0

    def checkDegat(self, bombe):
        for player in self.playerList:
            if abs(player.position[0] - bombe.position[0]) <= bombe.porte:
                player.hurt(bombe.power)
            if abs(player.position[1] - bombe.position[1]) <= bombe.porte:
                player.hurt(bombe.power)

        affectedCaseList = list(range(-int(bombe.porte), bombe.porte))

        for i in affectedCaseList:
            if bombe.position[0] + i >= 0 and bombe.position[0] + i <= self.maps.dim[0]:
                self.maps.matrice[bombe.position[0]+i][bombe.position[1]].hurt()

        for i in affectedCaseList:
            if bombe.position[1] + i >= 0 and bombe.position[1] + i <= self.maps.dim[1]:
                self.maps.matrice[bombe.position[0]][bombe.position[1]+i].hurt()

    def refresh(self):
        for i,player in enumerate(self.playerList):
            if player.refresh() == 0:
                bombeList[i].activateBombe(player.position)
            if player.refresh() == -1:
                if self.checkMove(player) == 0:
                    player.moveOK()
                else:
                    player.moveBack()

        for bombe in self.bombeList:
            if bombe.refresh() == 2:
                checkDegat(bombe)


        self.maps.refresh()


def testMoteur():
    game = Moteur('../Maps/map1.map', 1)
    while 1:
        game.refresh()


if __name__=='__main__':
    testMoteur()