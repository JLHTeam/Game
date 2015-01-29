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

    def refresh(self):
        self.game.refresh()
        if self.game._activation:
            pass #play sound et load gif
        if self.game._explosion:
            pass #play sound et load gif
        #print(ctrl.game.playerList[0].health)

    def newGame(self):
        self.game = Moteur(self.fileNameMap, self.modeGame)
        self.timer = QTimer()
        self.timer.timeout.connect(self.refresh)
        self.timer.start((1/FPS)*1000)

    def defineMap(self, fileNameMap):
        self.fileNameMap = fileNameMap

    def defineModeGame(self, modeGame):
        self.modeGame = modeGame

    def setAction(self, commande):
        if commande == Qt.Key_Z:
            self.game.setAction(1,1)
        if commande == Qt.Key_Up:
            self.game.setAction(1,0)
        if commande == Qt.Key_Q:
            self.game.setAction(2,1)
        if commande == Qt.Key_Left:
            self.game.setAction(2,0)
        if commande == Qt.Key_S:
            self.game.setAction(3,1)
        if commande == Qt.Key_Down:
            self.game.setAction(3,0)
        if commande == Qt.Key_D:
            self.game.setAction(4,1)
        if commande == Qt.Key_Right:
            self.game.setAction(4,0)
        if commande == Qt.Key_Enter:
            self.game.setAction(5,1)
        if commande == Qt.Key_Space:
            self.game.setAction(5,0)

    def getPosPlayer(self):
        pass

    def getPosBombe(self):
        return

    def getPosPlayer(self):
        pass

    def getPosWall(self):
        pass


if __name__=='__main__':
    app = QCoreApplication([])
    ctrl = ControllerGui()
    ctrl.defineMap('../Maps/map1.map')
    ctrl.defineModeGame("PvP")
    ctrl.newGame()
    ctrl.setAction(Qt.Key_Space)
    app.exec()