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

from controller import *
import sys


class VueDessin(QGraphicsView):

    def __init__(self, parent, controleur):
        super().__init__(parent)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scene = PongScene(self, controleur)
        self.setScene(self.scene)

    def resizeEvent(self, event):
        self.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio)

class PongScene(QGraphicsScene):

    def __init__(self, parent, controleur):
        super().__init__(parent)
        self.controleur = controleur
        self.controleur.inscrire(self)
        self.creer_dessin()

    def creer_dessin(self):
        self.setSceneRect(0, 0, 1, 1)
        brosse_noire = QBrush(QColor(0, 0, 0))
        brosse_blanche = QBrush(QColor(255, 255, 255))
        aucun_contour = QPen(Qt.NoPen)
        self.addRect(0, 0, 1, 1, aucun_contour, brosse_noire)
        self.raquette_g = self.addRect(0, 0, 0, 0, aucun_contour, brosse_blanche)
        self.raquette_d = self.addRect(0, 0, 0, 0, aucun_contour, brosse_blanche)
        self.balle = self.addEllipse(0, 0, 0, 0, aucun_contour, brosse_blanche)

    def rafraichir(self):
        pass

    def keyPressEvent(self, keyboard):
        key = keyboard.key()
        if key == Qt.Key_A: self.controleur.déplacer_raquette('GAUCHE', 'UP')
        if key == Qt.Key_Q: self.controleur.déplacer_raquette('GAUCHE', 'DOWN')
        if key == Qt.Key_9: self.controleur.déplacer_raquette('DROITE', 'UP')
        if key == Qt.Key_6: self.controleur.déplacer_raquette('DROITE', 'DOWN')

    def keyReleaseEvent(self, keyboard):
        key = keyboard.key()
        if key == Qt.Key_A or key == Qt.Key_Q: self.controleur.arrêter_raquette('GAUCHE')
        if key == Qt.Key_9 or key == Qt.Key_6: self.controleur.arrêter_raquette('DROITE')


def test():
    app = QApplication([])
    app.exec()

if __name__ == '__main__':
    test()