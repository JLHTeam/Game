import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
 
app=QApplication([])


class JeuWindow(QMainWindow):
        def __init__(self,controller):
                super().__init__()
                self.setWindowTitle('BomberMan JLHTeam_Menu')
                scene_widget = SceneWidget(self, controller)
                self.setCentralWidget(scene_widget)
                

class Controller:
        def __init__(self):
                self.message='Hi! '


class SceneWidget(QWidget):
            def __init__(self,parent, controller):
                 super().__init__()
                 self.controller = controller
                 layoutV = QVBoxLayout()
                 texte = QLabel('MENU PRINCIPAL : Bienvenue dans BomberMan JLHTeam!')
                 texte.setStyleSheet("color : yellow; font-weight: bold")
                 self.zone_texte=QTextEdit(controller.message)
 #                self.zone_texte.setReadOnly(True)
                 #self.zone_texte.setStyleSheet("background-image: url(./image/Neo Bomberman-acouper.png); color:white")
                 self.zone_texte.setAlignment(Qt.AlignHCenter)
 #                self.zone_texte.setStyleSheet("QTextEdit {color:white}")
 #                layoutV.addWidget(WidgetDessin(self,controller))
                 bouton_widget=Boutons(self, self.controller)  #2 lignes à enlever qd resolue image en fond et non devant..!!!
                 bouton_widget.setStyleSheet("border : None ; font-weight: bold 30px") #que le tour:  border-style: outset
                 layoutV.addWidget(bouton_widget)
                 layoutV.addWidget(texte)
  #               layoutV.addWidget(self.zone_texte)
                 self.setLayout(layoutV)
                 self.zone_texte.show()
                
class Boutons(QWidget):
            def __init__(self,parent, controller):
                 super().__init__()
                 self.controller = controller
                 layoutV=QVBoxLayout()
                 self.bouton1= QPushButton('Démarrer une Partie',self)
                 self.bouton2= QPushButton('Charger une Partie',self)
                 self.bouton3= QPushButton('Options',self)
                 self.bouton4= QPushButton('Quitter',self)
                 layoutV.addWidget(self.bouton1)
                 layoutV.addWidget(self.bouton2)
                 layoutV.addWidget(self.bouton3)
                 layoutV.addWidget(self.bouton4)
                 self.setLayout(layoutV)
                 
 

def main():
        app=QApplication(sys.argv)
        controller = Controller()
        fenetre= JeuWindow(controller)
        palette	= QPalette()
        palette.setBrush(QPalette.Background,QBrush(QPixmap("./image/bomberman_explosion.png")))
        fenetre.setPalette(palette)
        fenetre.setFixedSize(352,224)
        fenetre.show()
        app.exec()


if __name__ == '__main__':
    main()
