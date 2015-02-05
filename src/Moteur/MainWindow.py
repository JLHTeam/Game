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

import sys
from MenusWidget import *
from controller import *

class MainWindow(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        # 1 widget visible à la fois
        self.centralWidget = QStackedWidget(self)
        self.setCentralWidget(self.centralWidget)

        # Create widgets menu
        mainMenu = MenuWidget(self, self.controller)
        configGameMenu = configGameWidget(self, self.controller)
        widgetView = WidgetView(self, self.controller)

        # Add theses widget menu to the stack
        self.centralWidget.addWidget(mainMenu)
        self.centralWidget.addWidget(configGameMenu)
        self.centralWidget.addWidget(widgetView)


    def setMainWidget(self, index):
        self.centralWidget.setCurrentIndex(index)


def main():
    app = QApplication(sys.argv)
    timer = QTimer()
    ctrl = ControllerGui()
    music = Multimedia(ctrl)
    windows = MainWindow(ctrl)

    music.playGeneralSound()

    timer.timeout.connect(ctrl.refresh)
    timer.timeout.connect(music.refresh)

    ctrl.setMap('../Maps/map1.map')
    ctrl.setModeGame("PvP")
    ctrl.setAvatar('red')
    ctrl.setAvatar("blue")

    trl.setBombeForPLayer("TNT", 0)
    ctrl.setBombeForPLayer("TNT", 1)

    ctrl.newGame()


    timer.start((1/FPS)*1000)

    windows.setMainWidget(0)
    windows.show()
    app.exec()


if __name__ == '__main__':
    main()