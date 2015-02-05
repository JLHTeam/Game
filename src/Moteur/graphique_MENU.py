import sys
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
import graphique_ETAT_DEMARRAGE_PARTIE

app=QApplication([])


class JeuWindow(QMainWindow):
        def __init__(self, controller):
                super().__init__()
                self.setWindowTitle('BomberMan JLHTeam_Menu')
                scene_widget = SceneWidget(self, controller)
                self.setCentralWidget(scene_widget)
                

class Controller:
        def __init__(self):
                self.message ='Hi! '

        def on_ouvrir_1(self):
                fenetre = graphique_ETAT_DEMARRAGE_PARTIE.JeuWindow(self)
                palette	= QPalette()
                palette.setBrush(QPalette.Background,QBrush(QPixmap("./image/Bomberman.jpg")))
                fenetre.setPalette(palette)
                fenetre.setFixedSize(350,250)
                fenetre.show()
                app.exec()



class SceneWidget(QWidget):
            def __init__(self,parent, controller):
                 super().__init__()
                 self.controller = controller
                 layoutV = QVBoxLayout()
                 texte = QLabel('MENU PRINCIPAL : Bienvenue dans BomberMan JLHTeam!')
                 texte.setStyleSheet("color : yellow; font-weight: bold")
                 self.zone_texte = QTextEdit(controller.message)
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

                 self.bouton1.clicked.connect(self.on_bouton1)


            def on_bouton1(self):
                 self.connect(self.bouton1,SIGNAL('clicked()'),self.controller.on_ouvrir_1)


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
