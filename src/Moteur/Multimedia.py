__author__ = 'Hicham'


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

from random import *
from controller import *
import sys



class Multimedia():

    def __init__(self, controller ):
        self.controller = controller
        self.sounds = []
        self.loadAllSOund()

    def loadAllSOund(self):
        for fileNameSound in self.controller.soundGame:
            self.sounds.append(QSound(fileNameSound))
            print(fileNameSound)
        self.sounds.append(QSound(self.controller.soundExplosion))
        self.sounds.append(QSound(self.controller.soundActivation))
        self.sounds.append(QSound(self.controller.soundPlayerWin))
        self.sounds.append(QSound(self.controller.soundLoadMap))

    def refresh(self):
        if self.controller.game._activation:
            self.playActivationSound()
        if self.controller.game._explosion:
            self.playExplosionSound()

    def playGeneralSound(self):
        if len(self.sounds[:4]) > 0:
            choice(self.sounds[:4]).play()

    def playExplosionSound(self):
        self.sounds[4].play()

    def playActivationSound(self):
        self.sounds[5].play()

    def playPlayerWinSound(self):
        self.sounds[6].play()

    def playLoadMapSound(self):
        self.sounds[7].play()

if __name__=='__main__':
    app = QCoreApplication([])
    ctrl = ControllerGui()
    ctrl.setMap('../Maps/map1.map')
    ctrl.setModeGame("PvP")
    ctrl.newGame()
    music = Multimedia(ctrl)
    music.playGeneralSound()
    music.playPlayerWinSound()
    app.exec()