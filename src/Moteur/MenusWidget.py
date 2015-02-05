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


class MenuWidget(QWidget):
    def __init__(self, parent, controller):
        super().__init__()
        self.controller = controller
        self.initWidget()
        self.initLayout()

    def initWidget(self):
        # widget
        self.startQPB = QPushButton('Démarrer une Partie', self)
        self.loadQPB = QPushButton('Charger une Partie', self)
        self.optionsQPB = QPushButton('Options', self)
        self.exitQPB = QPushButton('Quitter', self)

    def initLayout(self):
        # layout
        layoutV = QVBoxLayout()
        layoutV.addWidget(self.startQPB)
        layoutV.addWidget(self.loadQPB)
        layoutV.addWidget(self.optionsQPB)
        layoutV.addWidget(self.exitQPB)
        self.setLayout(layoutV)

class configGameWidget(QWidget):
    def __init__(self, parent, controller):
        super().__init__()
        self.controller = controller

        # widget
        self.startQPB = QPushButton('Démarrer une Partie', self)
        self.loadQPB = QPushButton('Charger une Partie', self)
        self.optionsQPB = QPushButton('Options', self)
        self.exitQPB = QPushButton('Quitter', self)

        # layout
        layoutV = QVBoxLayout()
        layoutV.addWidget(self.startQPB)
        layoutV.addWidget(self.loadQPB)
        layoutV.addWidget(self.optionsQPB)
        layoutV.addWidget(self.exitQPB)
        self.setLayout(layoutV)

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

def main():
    app = QApplication(sys.argv)
    windows = MenuWidget(None)
    windows.show()
    app.exec()


if __name__ == '__main__':
    main()