import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
 
app=QApplication([])


class JeuWindow(QMainWindow):
        def __init__(self,controller):
                super().__init__()
                self.setWindowTitle('BomberMan JLHTeam_Jeu')
                scene_widget = SceneWidget(self, controller)
                self.setCentralWidget(scene_widget)

                
class SceneWidget(QWidget):
            def __init__(self,parent, controller):
                 super().__init__()
                 self.controller = controller
                 layoutV = QVBoxLayout()
                 texte = QLabel('MENU PRINCIPAL : Bienvenue dans BomberMan JLHTeam!')
                 texte.setStyleSheet("color : yellow; font-weight: bold")
                 self.zone_texte=QTextEdit(controller.message)
                 self.zone_texte.setReadOnly(True)
                 #self.zone_texte.setStyleSheet("background-image: url(./image/Neo Bomberman-acouper.png); color:white")
                 self.zone_texte.setAlignment(Qt.AlignHCenter)
                 self.zone_texte.setStyleSheet("QTextEdit {color:white}")
                 layoutV.addWidget(WidgetDessin(self,controller))
                 bouton_widget=Boutons(self, self.controller)  #2 lignes à enlever qd resolue image en fond et non devant..!!!
                 bouton_widget.setStyleSheet("border : None ; font-weight: bold 30px") #que le tour:  border-style: outset
                 layoutV.addWidget(bouton_widget)
                 layoutV.addWidget(texte)
                 layoutV.addWidget(self.zone_texte)
                 self.setLayout(layoutV)
                 self.zone_texte.show()
                
class Boutons(QWidget):
            def __init__(self,parent, controller):
                 super().__init__()
                 self.controller = controller
                 layoutV=QVBoxLayout()
                 self.bouton1= QPushButton('JEU_OPTION',self)
                 self.bouton2= QPushButton('JEU_QUITTER',self)
                 layoutV.addWidget(self.bouton1)
                 layoutV.addWidget(self.bouton2)
                 self.setLayout(layoutV)                 

class ElementsWidget(QWidget):
            def __init__(self,parent, controller):
                 super().__init__()
                 self.controller = controller

class MapWidget(QWidget):
        def ___init__(self,parent,controller):
                super().__init__()
                self.controller=controller

class Controller:
        def __init__(self):
                self.message='Hi! '
                
class WidgetDessin(QGraphicsView):
        def __init__(self, parent, controller):
                   super().__init__()
                   self.controller = controller
                   self.setScene(self.dessiner())
                             
        def dessiner(self):
                 scene = QGraphicsScene()
                 scene.setSceneRect(0, 0, 320, 320)
                 self.fond = QLabel(self)
   #                self.fond.setPixmap(QPixmap('image/bombermanTeam.jpg'))
 #                self.fond.setStyleSheet("background-image: url(./image/bombermanTeam.jpg)")  
 #                bouton_widget=Boutons(self, self.controller)
 #                scene.addWidget(bouton_widget)
   #                self.fond.setAlignment(Qt.AlignHCenter)

 #               texte = scene.addText("Hello, world!")
 #               scene.addLine(50, 50, 200, 200)
 #               stylo = QPen(Qt.blue, 5, Qt.SolidLine)
 #               scene.addEllipse(200,100,20,20, stylo)
 #               brosse = QBrush(QColor(128,0,128), Qt.SolidPattern)
 #               scene.addRect(100,200,50,50, stylo,brosse)
                 return scene

def main():
        app=QApplication(sys.argv)
        controller = Controller()
        fenetre= JeuWindow(controller)
 #       palette	= QPalette()
 #       palette.setBrush(QPalette.Background,QBrush(QPixmap("./image/bomberman_explosion.png")))
 #        fenetre.setPalette(palette)
 #       fenetre.setFixedSize(352,224)
        fenetre.show()
        app.exec()


if __name__ == '__main__':
    main()


                 
