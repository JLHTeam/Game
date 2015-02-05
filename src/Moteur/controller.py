try:
    # Qt5
    from PyQt5.QtCore import *
    from PyQt5.QtGui import *
    from PyQt5.QtWidgets import *
    from PyQt5.QtMultimedia import *
except ImportError:
    try:
        # Qt4
        from PyQt4.QtCore import *
        from PyQt4.QtGui import *
    except ImportError:
        print('Merci d\'installer PyQt5 ou PyQt4.')
        exit()

from moteur import *
from Multimedia import *
import os

"""\brief
	Moteur class

    The detailed description of the class would appear right here.
"""

FPS = 60

class ControllerBase:
    def __init__(self):
        self.clients = []
        self.message = None

    def inscrire(self, client):
        self.clients.append(client)

    def avertir(self):
        for client in self.clients:
            client.rafraichir()

    def info(self):
        return self.message


class ControllerGui(ControllerBase):
    def __init__(self):
        super().__init__()
        self.initSound()
        self.fileNameAvatar = ["", ""]
        self.bombePlayer = ["", ""]

    def initSound(self):
        path = "../sounds/"
        extension = ".wav"
        self.soundGeneralStatut = 1
        self.soundEventStatut = 1
        self.soundExplosion = path + "sound_bombeExplosion" + extension
        self.soundActivation = path + "sound_bombePlanted" + extension
        self.soundPlayerWin = path + "sound_win" + extension
        self.soundLoadMap = path + "sound_loadMap" + extension
        self.soundGame = []

        for i in range(4):
            self.soundGame.append(path + "sound_gen_" + str(i) + extension)

    def setBombe(self, bombeType, numPlayer):
        self.bombePlayer[numPlayer-1] = bombeType

    def setAvatar(self, color, numPlayer):
        self.fileNameAvatar[numPlayer-1] = color

    def refresh(self):
        self.game.refresh()

    def newGame(self):
        self.game = Moteur(self.fileNameMap, self.modeGame, self.bombePlayer)

    def setMap(self, fileNameMap):
        self.fileNameMap = fileNameMap

    def setModeGame(self, modeGame):
        self.modeGame = modeGame

    def getAvatar(self):
        return self.fileNameAvatar

    def setAction(self, commande):
        if commande == Qt.Key_Z:
            self.game.setAction("H",1)
        if commande == Qt.Key_Up:
            self.game.setAction("H",0)
        if commande == Qt.Key_Q:
            self.game.setAction("G",1)
        if commande == Qt.Key_Left:
            self.game.setAction("G",0)
        if commande == Qt.Key_S:
            self.game.setAction("B",1)
        if commande == Qt.Key_Down:
            self.game.setAction("B",0)
        if commande == Qt.Key_D:
            self.game.setAction("D",1)
        if commande == Qt.Key_Right:
            self.game.setAction("D",0)
        if commande == Qt.Key_Enter:
            self.game.setAction("BB",1)
        if commande == Qt.Key_Space:
            self.game.setAction("BB",0)

    def getPosPlayer(self):
        return [ posPlayer.position for posPlayer in self.game.playerList ]

    def getPosBombe(self):
        return [ posBombe.position for posBombe in self.game.bombeList ]

    def getPosWall(self):
        posWallList = []
        for x,line in enumerate(self.game.maps.matrice):
            for y,case in enumerate(line):
                if self.game.maps.matrice[x][y].sorte != 0:
                    posWallList.append([x,y])
        return posWallList

    def saveGame(self, filePath):
        if not os.path.exists(filePath):
            os.makedirs(filePath)
        fileSaveMap = open(filePath + "/saveMap.map", 'w+')
        fileSaveOther = open(filePath + "/saveOpt.map", 'w+')
        # sauvegarde de l'état de la map, des type de bombes en jeu, du mode de jeu
        fileSaveOther.write(self.modeGame + "\n" + self.bombePlayer[0] + "\n" +  self.bombePlayer[1])
        matrix = self.game.maps.saveMap()
        fileMap = csv.writer(fileSaveMap, delimiter = '\t', lineterminator = '\n')
        fileMap.writerows(matrix)


if __name__=='__main__':
    app = QCoreApplication([])

    timer = QTimer()
    ctrl = ControllerGui()
    ctrl.setMap('../Maps/map1.map')
    ctrl.setModeGame("PvP")
    ctrl.setBombe('TNT', 1)
    ctrl.setBombe('TNT', 2)
    ctrl.setAvatar("red", 1)
    ctrl.setAvatar("red", 2)
    ctrl.newGame()
    print(ctrl.game.maps.dim)
    ctrl.saveGame("../save/")
    music = Multimedia(ctrl)
    music.playGeneralSound()


    timer.timeout.connect(ctrl.refresh)
    timer.timeout.connect(music.refresh)
    #timer.start((1/FPS)*1000)

    ctrl.saveGame("../save/blbla")



    app.exec()