import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
 
app=QApplication([])


class JeuWindow(QMainWindow):
        def __init__(self,controller):
                super().__init__()
                self.setWindowTitle('BomberMan JLHTeam')

                scene_widget = SceneWidget(self, controller)
                self.setCentralWidget(scene_widget)

class Controller:
        def __init__(self):
                self.message='Hi!'
                
class WidgetDessin(QGraphicsView):
        def __init__(self, parent, controller):
                   super().__init__()
                   self.controller = controller
                   self.setScene(self.dessiner())
                   
           
        def dessiner(self):
                 scene = QGraphicsScene()
                 scene.setSceneRect(0, 0, 300, 168)
                 self.fond = QLabel(self)
                 self.fond.setPixmap(QPixmap('image/bombermanTeam.jpg'))
 #                self.fond.setStyleSheet("background-image: url(./image/bombermanTeam.jpg)")  
 #                bouton_widget=Boutons(self, self.controller)
 #                scene.addWidget(bouton_widget)
                 self.fond.setAlignment(Qt.AlignHCenter)


                 
 #               texte = scene.addText("Hello, world!")
 #               scene.addLine(50, 50, 200, 200)
 #               stylo = QPen(Qt.blue, 5, Qt.SolidLine)
 #               scene.addEllipse(200,100,20,20, stylo)
 #               brosse = QBrush(QColor(128,0,128), Qt.SolidPattern)
 #               scene.addRect(100,200,50,50, stylo,brosse)
                 return scene

class SceneWidget(QWidget):
            def __init__(self,parent, controller):
                 super().__init__()
                 self.controller = controller
                 layoutV=QVBoxLayout()
                 self.zone_texte=QTextEdit(controller.message)
                 self.zone_texte.setReadOnly(True)
                 layoutV.addWidget(WidgetDessin(self,controller))
                 bouton_widget=Boutons(self, self.controller)  #2 lignes à enlever qd resolue image en fond et non devant..!!!
                 layoutV.addWidget(bouton_widget)              ####
                 layoutV.addWidget(self.zone_texte)
                 self.setLayout(layoutV)
                 self.zone_texte.show()
                
class Boutons(QWidget):
            def __init__(self,parent, controller):
                 super().__init__()
                 self.controller = controller
                 layoutH=QHBoxLayout()
                 self.bouton1= QPushButton('Démarrer une Partie',self)
                 self.bouton2= QPushButton('Charger une Partie',self)
                 self.bouton3= QPushButton('Options',self)
                 self.bouton4= QPushButton('Quitter',self)
                 layoutH.addWidget(self.bouton1)
                 layoutH.addWidget(self.bouton2)
                 layoutH.addWidget(self.bouton3)
                 layoutH.addWidget(self.bouton4)
                 self.setLayout(layoutH)
                 
 
                      
class ElementsWidget(QWidget):
            def __init__(self,parent, controller):
                 super().__init__()
                 self.controller = controller

class MapWidget(QWidget):
        def ___init__(self,parent,controller):
                super().__init__()
                self.controller=controller
                
def main():
        app=QApplication(sys.argv)
        controller = Controller()
        fenetre= JeuWindow(controller)
        fenetre.show()
        app.exec()


if __name__ == '__main__':
    main()
