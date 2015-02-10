from PyQt4.QtCore import *
from PyQt4.QtGui import *
##except ImportError:
##        print('Merci d\'installer PyQt5 ou PyQt4.')
##        exit()

from controller import *
import sys
from map import*


class MainWindow(QMainWindow):
    def __init__(self, controller, timer):
        super().__init__()
        self.setWindowTitle('BomberMan JLHTeam')
        self.controller = controller
        widget = JeuWindow(self, self.controller)
        self.setCentralWidget(widget)
        self.timer = timer
        

class SceneView(QGraphicsView):
        def __init__(self, parent, controller):
            super().__init__()
            self.controller = controller
            self.carte = Carte("../Maps/map1.map")
            self.carte.loadMap()
            self.carte.saveMap()
            self.carte.refresh()
            self.setScene(self.dessiner())


        def dessiner(self):
            self.scene = QGraphicsScene()
            self.scene.setSceneRect(0, 0, 448, 448)

           
            for i in range(14):
                self.line=[]
                for j in range(14):
                
                    self.line.append(QLabel(self))
  #                  self.line[-1].setAlignment(Qt.AlignHCenter)
                    self.line[-1].setPixmap(QPixmap('../carres/bleu.png'))
                    
                for line in self.line:

                       line.setPos( i*32, j*32) 
                       self.scene.addWidget(line)


                
 #               for j in range(14):
 #                   self.pix[i][j] = QPixmap('../carres/bleu.png')
 #                   self.scene.addWidget(self.pix[i][j])


            #for i,line in enumerate(self.carte.matrice):
                #for j,element in enumerate(line):
       #             if element.sorte == 0:
 #           self.pix = QGraphicsPixmapItem(None, self.scene)
 #           self.pix = QtGui.QPixmap(QtCore.QSize(self.size + 4, self.size + 4))
 #                   element.setPixmap(QPixmap( '../carres/bleu.png'))
 #                   self.scene.addWidget(element)
                    

                              
 #                   self.scene.addWidget()
                    


        #                self.fond.setPixmap(QPixmap('image/bombermanTeam.jpg'))
        #                self.fond.setStyleSheet("background-image: url(./image/bombermanTeam.jpg)")
        #                bouton_widget=Boutons(self, self.controller)
        #                scene.addWidget(bouton_widget)
        #                self.fond.setAlignment(Qt.AlignHCenter)

        #               texte = scene.addText("Hello, world!")
  #          self.scene.addLine(50, 50, 200, 200)
        #               stylo = QPen(Qt.blue, 5, Qt.SolidLine)
        #               scene.addEllipse(200,100,20,20, stylo)
 #           brosse = QBrush(QColor(128,0,128), Qt.SolidPattern)
#            self.scene.addRect(100,200,50,50, stylo,brosse)
            return self.scene

##class CatreWidget(QWidget):
##            def __init__(self, parent, controller):
##            super().__init__()
##            self.controller = controller
##
##            self.carte = Carte('../Maps/map1.map')
##            self.carte.loadMap()
##            self.carte.saveMap()
##            self.carte.refresh()
##
##            for element in self.carte:
##                if element.sorte == 0:
                    

    


class JeuWindow(QFrame):
    def __init__(self, parent, controller):
            super().__init__()

            self.controller = controller
            self.initWidget()
            self.setWidget()

    def initWidget(self):
            self.layoutV = QVBoxLayout()
            self.texte = QLabel('Essai')
            self.scene = SceneView( self, self.controller)

    def setWidget(self):
            self.layoutV.addWidget(self.texte)
            self.layoutV.addWidget(self.scene)
            self.setLayout(self.layoutV)


def main():
    app = QApplication(sys.argv)
    controller = ControllerGui()
    timer = QTimer()
    fenetre = MainWindow(controller, timer)
    #print(fenetre.carte.matrice[1][1].sorte)


    ##        palette = QPalette()
    ##        palette.setBrush(QPalette.Background,QBrush(QPixmap("../image/bomberman_explosion.png")))
    ##        fenetre.setPalette(palette)
    ##        fenetre.setFixedSize(352,224)
    fenetre.show()
    app.exec()


if __name__ == '__main__':
    main()
