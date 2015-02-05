__author__ = 'Hicham'

##try:
##    # Qt5
##    from PyQt5.QtCore import *
##    from PyQt5.QtGui import *
##    from PyQt5.QtWidgets import *
##    from PyQt5.QtMultimedia import *
##except ImportError:
    try:
        # Qt4
        from PyQt4.QtCore import *
        from PyQt4.QtGui import *
    except ImportError:
        print('Merci d\'installer PyQt5 ou PyQt4.')
        exit()

from controller import *
import sys


class WidgetView(QGraphicsView):

    def __init__(self, parent, controller ):
        super().__init__(parent)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scene = PongScene(self, controller)
        self.setScene(self.scene)

    def refresh(self):
        pass

    def resizeEvent(self, event):
        self.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio)

class PongScene(QGraphicsScene):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.initDraw()

    def initDraw(self):
        pass

    def refresh(self):
        pass

    def keyPressEvent(self, keyboard):
        key = keyboard.key()
        self.controller.setAction(key)

def test():
    app = QApplication([])

    timer = QTimer()
    ctrl = ControllerGui()
    music = Multimedia(ctrl)
    widgetView = WidgetView(None, ctrl)

    timer.timeout.connect(ctrl.refresh)
    timer.timeout.connect(music.refresh)
    timer.timeout.connect(widgetView.refresh)

    music.playGeneralSound()
    ctrl.setMap('../Maps/map1.map')
    ctrl.setModeGame("PvP")
    ctrl.setAvatar('red')
    ctrl.setAvatar("blue")
    ctrl.newGame()
    ctrl.setBombeForPLayer("TNT", 0)
    ctrl.setBombeForPLayer("TNT", 1)

    timer.start((1/FPS)*1000)

    widgetView.show()
    app.exec()

if __name__ == '__main__':
    test()
