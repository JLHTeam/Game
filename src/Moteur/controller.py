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


    def refresh(self):
        self.game.refresh()
        #print(ctrl.game.playerList[0].health)

    def newGame(self):
        self.game = Moteur(self.fileNameMap, self.modeGame)

    def setMap(self, fileNameMap):
        self.fileNameMap = fileNameMap

    def setModeGame(self, modeGame):
        self.modeGame = modeGame

    def setAvatar(self, fileNameAvatar):
        self.fileNameAvatar = fileNameAvatar

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


if __name__=='__main__':
    app = QCoreApplication([])

    timer = QTimer()
    ctrl = ControllerGui()
    ctrl.setMap('../Maps/map1.map')
    ctrl.setModeGame("PvP")
    ctrl.newGame()
    music = Multimedia(ctrl)
    #music.playGeneralSound()


    timer.timeout.connect(ctrl.refresh)
    timer.timeout.connect(music.refresh)
    timer.start((1/FPS)*1000)

    i = 0
    while i < 10000000:
        i += 1

    ctrl.setAction(Qt.Key_Space)



    print(ctrl.getPosWall())
    print(ctrl.getPosPlayer())
    print(ctrl.getPosBombe())
    app.exec()