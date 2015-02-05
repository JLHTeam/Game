import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Controller_graphique import Controller

app=QApplication([])


class SceneWindow(QMainWindow):
        def __init__(self,controller):
                super().__init__()
                self.setWindowTitle('BomberMan JLHTeam_Menu')
                self.definir_fenetre_principale(self)
                self.controller = controller
                menu_widget = MenuWidget(self, self.controller)
                self.setCentralWidget(menu_widget)
                
        def setWidget(self, widget):
                self.setCentralWidget(widget)

        def definir_fenetre_principale(self,widget):
                self.fenetre=widget

        def demarrerPartie(self):
                demarrer_widget = DemarrerWidget(self.fenetre,self.controller)
                self.fenetre.setWidget(demarrer_widget)

        def chargerPartie(self):
   ###Faire choisir parmi des configuration puis stocker les elments
                jeu_widget = JeuWindow(self.fenetre,self)
                self.fenetre.setWidget(jeu_widget)
                pass

        def back(self):
                menu_widget = MenuWidget(self.fenetre,self.controller)
                self.fenetre.setWidget(menu_widget)

        def jouer(self):
                jeu_widget = JeuWindow(self.fenetre,self.controller)
                self.fenetre.setWidget(jeu_widget)


class MenuWidget(QFrame):
            def __init__(self,parent, controller):
                 super().__init__()
                 self.controller = controller
                 self.parent = parent
                 self.initWidget()
                 self.setStyleWidget()
                 self.setWidget()
                 self.setConnection()

            def initWidget(self):
                 self.layoutV = QVBoxLayout()
                 self.texte = QLabel('MENU PRINCIPAL : Bienvenue dans BomberMan JLHTeam!')
                 self.initPartieQP= QPushButton('Démarrer une Partie',self)
                 self.chargerPartieQP= QPushButton('Charger une Partie',self)
                 self.optionsQP= QPushButton('Options',self)
                 self.quitterQP= QPushButton('Quitter',self)

            def setStyleWidget(self):
                 self.initPartieQP.setStyleSheet("border : None ; font-weight: bold 30px")
                 self.chargerPartieQP.setStyleSheet("border : None ; font-weight: bold 30px")
                 self.optionsQP.setStyleSheet("border : None ; font-weight: bold 30px")
                 self.quitterQP.setStyleSheet("border : None ; font-weight: bold 30px")
                 self.texte.setStyleSheet("color : yellow; font-weight: bold")
                 self.setStyleSheet("MenuWidget{background-image: url(./image/bomberman_explosion.png); color:white}")
                 image = QPixmap("./image/bomberman_explosion.png")
                 size = image.width()
                 self.parent.setFixedSize(352,224)

            def setWidget(self):
                 self.layoutV.addWidget(self.initPartieQP)
                 self.layoutV.addWidget(self.chargerPartieQP)
                 self.layoutV.addWidget(self.optionsQP)
                 self.layoutV.addWidget(self.quitterQP)
                 self.layoutV.addWidget(self.texte)
                 self.setLayout(self.layoutV)

            def setConnection(self):
                 self.initPartieQP.clicked.connect(self.DemarrerOuvrir)
                 self.chargerPartieQP.clicked.connect(self.MenuCharger)


            def DemarrerOuvrir(self):
                 self.connect(self.initPartieQP,SIGNAL('clicked()'),self.parent.demarrerPartie)

            def MenuCharger(self):
                 self.connect(self.chargerPartieQP,SIGNAL('clicked()'),self.parent.chargerPartie)


class DemarrerWidget(QFrame):
            def __init__(self,parent, controller):
                 super().__init__()
                 self.controller = controller
                 self.parent = parent
                 self.initWidget()
                 self.setStyleWidget()
                 self.setWidget()
                 self.setConnection()

            def initWidget(self):
                 self.mainLayoutV = QVBoxLayout()
                 self.layoutH = QHBoxLayout()
                 self.layoutH2 = QHBoxLayout()
                 self.layoutH3 = QHBoxLayout()
                 self.layoutHBombe = QHBoxLayout()
                 self.PVPQP = QPushButton('Joueur VS Joueur',self)
                 self.PVEQP = QPushButton('Joueur VS Ordinateur',self)
                 self.backQP = QPushButton('Revenir à l’écran d’accueil',self) 
                 self.Map1QP = QPushButton(' Map 1 ',self)
                 self.Map2QP  = QPushButton('Map 2',self)
                 self.Map3QP  = QPushButton('Map 3',self)
                 self.indicationMap = QLabel('Choisir la Map')
                 self.indicationJoueur = QLabel('Choisir un Joueur')
                 self.avatarRedQP = QPushButton('Avatar red',self)
                 self.avatarBlueQP = QPushButton('Avatar blue',self)
                 self.avatarGreenQP = QPushButton('Avatar green',self)
                 self.TNTQP = QPushButton('TNT',self)
                 self.dynamiteQP = QPushButton('Dynamite',self)
                 self.bombeHQP = QPushButton('Bombe H',self)
                 self.DemarrerPartieQP = QPushButton('Démarrer la Partie',self)
                 self.indicationBombe = QLabel('Choisir une Bombe')
                 self.status=0

            def setStyleWidget(self):
                 self.PVEQP.setStyleSheet("border : None ; font-weight: bold 30px") #que le tour:  border-style: outset 
                 self.PVPQP.setStyleSheet("border : None ; font-weight: bold 30px")
                 self.backQP.setStyleSheet("border : None ; font-weight: bold 30px")
                 self.Map1QP.setStyleSheet("border : None ; font-weight: bold 30px")
                 self.Map2QP.setStyleSheet("border : None ; font-weight: bold 30px")
                 self.Map3QP.setStyleSheet("border : None ; font-weight: bold 30px")
                 self.avatarRedQP .setStyleSheet("border : None ; font-weight: bold 30px")
                 self.avatarBlueQP .setStyleSheet("border : None ; font-weight: bold 30px")
                 self.avatarGreenQP.setStyleSheet("border : None ; font-weight: bold 30px")
                 self.TNTQP .setStyleSheet("border : None ; font-weight: bold 30px")
                 self.dynamiteQP .setStyleSheet("border : None ; font-weight: bold 30px")
                 self.bombeHQP.setStyleSheet("border : None ; font-weight: bold 30px")
                 self.setStyleSheet("DemarrerWidget{background-image: url(./image/Bomberman.jpg); color:white}")
                 self.parent.setFixedSize(400,300)


            def setWidget(self):
                 self.layoutH.addWidget(self.PVPQP)
                 self.layoutH.addWidget(self.PVEQP)
                 self.mainLayoutV.addLayout(self.layoutH)
                 self.layoutH2.addWidget(self.indicationMap)
                 self.layoutH2.addWidget(self.Map1QP )
                 self.layoutH2.addWidget(self.Map2QP )
                 self.layoutH2.addWidget(self.Map3QP )
                 self.mainLayoutV.addLayout(self.layoutH2)
                 self.layoutH3.addWidget(self.indicationJoueur)
                 self.layoutH3.addWidget(self.avatarRedQP)
                 self.layoutH3.addWidget(self.avatarBlueQP)
                 self.layoutH3.addWidget(self.avatarGreenQP)
                 self.mainLayoutV.addLayout(self.layoutH3)
                 self.layoutHBombe.addWidget(self.indicationBombe)
                 self.layoutHBombe.addWidget(self.TNTQP)
                 self.layoutHBombe.addWidget(self.dynamiteQP)
                 self.layoutHBombe.addWidget(self.bombeHQP)
                 self.mainLayoutV.addLayout(self.layoutHBombe)
                 self.mainLayoutV.addWidget(self.backQP)
                 self.mainLayoutV.addWidget(self.DemarrerPartieQP)
                 self.setLayout(self.mainLayoutV)
                 
            def setConnection(self):
                 self.PVPQP .clicked.connect(self.onPVP)
                 self.PVEQP .clicked.connect(self.onPVE)
                 self.Map1QP .clicked.connect(self.onMap1)
                 self.Map2QP .clicked.connect(self.onMap2)
                 self.Map3QP .clicked.connect(self.onMap3)
                 self.avatarRedQP.clicked.connect(self.onAvatarRed)
                 self.avatarBlueQP.clicked.connect(self.onAvatarBlue)
                 self.avatarGreenQP.clicked.connect(self.onAvatarGreen)
                 self.TNTQP.clicked.connect(self.onTNT)
                 self.dynamiteQP.clicked.connect(self.onDynamite)
                 self.bombeHQP.clicked.connect(self.onBombeH)
                 self.backQP.clicked.connect(self.backBouton)
                 self.DemarrerPartieQP.clicked.connect(self.on_jouer)
                 self.DemarrerPartieQP.setDisabled(1)


            def onPVP(self):
                self.PVPQP.setStyleSheet(" font-weight: bold 30px ;  border-style: outset ; color : brown")
                self.PVEQP.setDisabled(1)
                self.status+=1;
                self.check_status()

            def onPVE(self):
                self.PVEQP.setStyleSheet(" font-weight: bold 30px ;  border-style: outset ; color : brown")
                self.PVPQP.setDisabled(1)
                self.status+=1;
                self.check_status()

            def onAvatarRed(self):
                self.avatarRedQP.setStyleSheet(" font-weight: bold 30px ;  border-style: outset ; color : pink")
                self.avatarBlueQP.setDisabled(1)
                self.avatarGreenQP.setDisabled(1)
                self.status+=1;
                Avatar='A1'
                self.controller.setAvatar(Avatar)
                self.check_status()
                
            def onAvatarBlue(self):
                self.avatarBlueQP.setStyleSheet(" font-weight: bold 30px ;  border-style: outset ; color : pink")
                self.avatarRedQP.setDisabled(1)
                self.avatarGreenQP.setDisabled(1)
                self.status+=1;
                Avatar='A2'
                self.controller.setAvatar(Avatar)
                self.check_status()

            def onAvatarGreen(self):
                self.avatarGreenQP.setStyleSheet(" font-weight: bold 30px ;  border-style: outset ; color : pink")
                self.avatarRedQP.setDisabled(1)
                self.bavatarBlueQP.setDisabled(1)
                self.status+=1;
                Avatar='A3'
                self.controller.setAvatar(Avatar)
                self.check_status()
                

            def onMap1(self):
                self.Map1QP .setStyleSheet(" font-weight: bold 30px ;  border-style: outset ; color : pink")
                self.Map2QP .setDisabled(1)
                self.Map3QP .setDisabled(1)
                self.status+=1;
                Map='Map1'
                self.controller.setMap(Map)
                self.check_status()
                
            def onMap2(self):
                self.Map2QP .setStyleSheet(" font-weight: bold 30px ;  border-style: outset ; color : pink")
                self.Map1QP .setDisabled(1)
                self.Map3QP .setDisabled(1)
                self.status+=1;
                Map='Map2'
                self.controller.setMap(Map)
                self.check_status()

            def onMap3(self):
                self.Map3QP .setStyleSheet(" font-weight: bold 30px ;  border-style: outset ; color : pink")
                self.Map1QP .setDisabled(1)
                self.Map2QP .setDisabled(1)
                self.status+=1;
                Map='Map3'
                self.controller.setMap(Map)
                self.check_status()

            def onTNT(self):
                self.TNTQP .setStyleSheet(" font-weight: bold 30px ;  border-style: outset ; color : pink")
                self.dynamiteQP .setDisabled(1)
                self.bombeHQP .setDisabled(1)
                self.status+=1;
                Bombe='TNT'
                self.controller.setBombe(Bombe)
                self.check_status()
                
            def onDynamite(self):
                self.dynamiteQP .setStyleSheet(" font-weight: bold 30px ;  border-style: outset ; color : pink")
                self.TNTQP .setDisabled(1)
                self.bombeHQP .setDisabled(1)
                self.status+=1;
                Bombe='Dynamite'
                self.controller.setBombe(Bombe)
                self.check_status()

            def onBombeH(self):
                self.bombeHQP .setStyleSheet(" font-weight: bold 30px ;  border-style: outset ; color : pink")
                self.TNTQP .setDisabled(1)
                self.dynamiteQP .setDisabled(1)
                self.status+=1;
                Bombe='BombeH'
                self.controller.setBombe(Bombe)
                self.check_status()


            def backBouton(self):
                 self.connect(self.backQP,SIGNAL('clicked()'),self.parent.back)

            def check_status(self):
                 if self.status==4:
                    self.DemarrerPartieQP.setDisabled(0)

            def on_jouer(self):
                    self.connect(self.DemarrerPartieQP,SIGNAL('clicked()'),self.parent.jouer)


class Boutons(QWidget):
            def __init__(self,parent, controller):
                 super().__init__()
                 self.controller = controller
                 self.parent = parent

class ElementsWidget(QWidget):
            def __init__(self,parent, controller):
                 super().__init__()
                 self.controller = controller

class MapWidget(QWidget):
        def ___init__(self,parent,controller):
                super().__init__()
                self.controller = controller

class JeuWindow(QGraphicsView):
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
        fenetre= SceneWindow(controller)
##        palette = QPalette()
##        palette.setBrush(QPalette.Background,QBrush(QPixmap("./image/bomberman_explosion.png")))
##        fenetre.setPalette(palette)
##        fenetre.setFixedSize(352,224)
        fenetre.show()
        app.exec()


if __name__ == '__main__':
    main()
