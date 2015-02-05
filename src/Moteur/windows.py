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



class MainWindow(QMainWindow):
    def __init__(self, controller, timer):
        super().__init__()
        self.setWindowTitle('BomberMan JLHTeam_Menu')
        self.definir_fenetre_principale(self)
        self.controller = controller
        menu_widget = MenuWidget(self, self.controller)
        self.setCentralWidget(menu_widget)
        self.timer = timer

    def setWidget(self, widget):
        self.setCentralWidget(widget)

    def definir_fenetre_principale(self,widget):
        self.fenetre = widget

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
        self.controller.newGame()
        timer.start(1/fps)


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
        self.initPartieQP = QPushButton('Démarrer une Partie',self)
        self.chargerPartieQP = QPushButton('Charger une Partie',self)
        self.optionsQP = QPushButton('Options',self)
        self.quitterQP = QPushButton('Quitter',self)

    def setStyleWidget(self):
        self.initPartieQP.setStyleSheet("border : None ; font-weight: bold;  font-size: 20pt;")
        self.chargerPartieQP.setStyleSheet("border : None ; font-weight: bold;  font-size: 20pt;")
        self.optionsQP.setStyleSheet("border : None ; font-weight: bold;  font-size: 20pt;")
        self.quitterQP.setStyleSheet("border : None ; font-weight: bold;  font-size: 20pt;")
        self.texte.setStyleSheet("color : yellow; font-weight: bold")
        self.setStyleSheet("MenuWidget{background-image: url(../image/bomberman_explosion.png); color:white}")
        image = QPixmap("../image/bomberman_explosion.png")
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
        self.initPartieQP.clicked.connect(self.parent.demarrerPartie)

    def MenuCharger(self):
        self.chargerPartieQP.clicked.connect(self.parent.chargerPartie)

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
        self.layoutVP1 = QVBoxLayout()
        self.layoutVP2 = QVBoxLayout()
        self.layoutHBox = QHBoxLayout()
        self.boxP1 = QGroupBox("Joueur 1")
        self.boxP2 = QGroupBox("Joueur 2")

        self.layoutHModeGame = QHBoxLayout()
        self.layoutHMap = QHBoxLayout()
        self.layoutHAvatarP1 = QHBoxLayout()
        self.layoutHBombeP1 = QHBoxLayout()
        self.layoutHAvatarP2 = QHBoxLayout()
        self.layoutHBombeP2 = QHBoxLayout()
        self.PVPQP = QPushButton('Joueur VS Joueur',self)
        self.PVEQP = QPushButton('Joueur VS Ordinateur',self)
        self.backQP = QPushButton('Revenir à l’écran d’accueil',self)
        self.Map1QP = QPushButton(' Map 1 ',self)
        self.Map2QP  = QPushButton('Map 2',self)
        self.Map3QP  = QPushButton('Map 3',self)
        self.indicationMap = QLabel('Choisir la Map')
        self.indicationJoueur = QLabel('Choisir un Joueur')
        self.avatarP1RedQP = QPushButton('Avatar red',self)
        self.avatarP1BlueQP = QPushButton('Avatar blue',self)
        self.avatarP1GreenQP = QPushButton('Avatar green',self)
        self.avatarP2RedQP = QPushButton('Avatar red',self)
        self.avatarP2BlueQP = QPushButton('Avatar blue',self)
        self.avatarP2GreenQP = QPushButton('Avatar green',self)
        self.TNTP1QP = QPushButton('TNT',self)
        self.dynamiteP1QP = QPushButton('Dynamite',self)
        self.bombeHP1QP = QPushButton('Bombe H',self)
        self.TNTP2QP = QPushButton('TNT',self)
        self.dynamiteP2QP = QPushButton('Dynamite',self)
        self.bombeHP2QP = QPushButton('Bombe H',self)
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
        self.avatarP1RedQP.setStyleSheet("border : None ; font-weight: bold 30px")
        self.avatarP1BlueQP.setStyleSheet("border : None ; font-weight: bold 30px")
        self.avatarP1GreenQP.setStyleSheet("border : None ; font-weight: bold 30px")
        self.TNTP1QP.setStyleSheet("border : None ; font-weight: bold 30px")
        self.dynamiteP1QP.setStyleSheet("border : None ; font-weight: bold 30px")
        self.bombeHP1QP.setStyleSheet("border : None ; font-weight: bold 30px")
        self.avatarP2RedQP.setStyleSheet("border : None ; font-weight: bold 30px")
        self.avatarP2BlueQP.setStyleSheet("border : None ; font-weight: bold 30px")
        self.avatarP2GreenQP.setStyleSheet("border : None ; font-weight: bold 30px")
        self.TNTP2QP.setStyleSheet("border : None ; font-weight: bold 30px")
        self.dynamiteP2QP.setStyleSheet("border : None ; font-weight: bold 30px")
        self.bombeHP2QP.setStyleSheet("border : None ; font-weight: bold 30px")
        self.setStyleSheet("DemarrerWidget{background-image: url(../image/Bomberman.jpg); color:white}")
        self.parent.setFixedSize(400,300)

    def setWidget(self):
        self.layoutHModeGame.addWidget(self.PVPQP)
        self.layoutHModeGame.addWidget(self.PVEQP)
        self.mainLayoutV.addLayout(self.layoutHModeGame)

        self.layoutHMap.addWidget(self.indicationMap)
        self.layoutHMap.addWidget(self.Map1QP )
        self.layoutHMap.addWidget(self.Map2QP )
        self.layoutHMap.addWidget(self.Map3QP )
        self.mainLayoutV.addLayout(self.layoutHMap)

        self.layoutHAvatarP1.addWidget(self.indicationJoueur)
        self.layoutHAvatarP1.addWidget(self.avatarP1RedQP)
        self.layoutHAvatarP1.addWidget(self.avatarP1BlueQP)
        self.layoutHAvatarP1.addWidget(self.avatarP1GreenQP)
        self.layoutHBombeP1.addWidget(self.indicationBombe)
        self.layoutHBombeP1.addWidget(self.TNTP1QP)
        self.layoutHBombeP1.addWidget(self.dynamiteP1QP)
        self.layoutHBombeP1.addWidget(self.bombeHP1QP)
        self.layoutVP1.addLayout(self.layoutHAvatarP1)
        self.layoutVP1.addLayout(self.layoutHBombeP1)
        self.boxP1.setLayout(self.layoutVP1)

        self.layoutHAvatarP2.addWidget(self.indicationJoueur)
        self.layoutHAvatarP2.addWidget(self.avatarP2RedQP)
        self.layoutHAvatarP2.addWidget(self.avatarP2BlueQP)
        self.layoutHAvatarP2.addWidget(self.avatarP2GreenQP)
        self.layoutHBombeP2.addWidget(self.indicationBombe)
        self.layoutHBombeP2.addWidget(self.TNTP2QP)
        self.layoutHBombeP2.addWidget(self.dynamiteP2QP)
        self.layoutHBombeP2.addWidget(self.bombeHP2QP)
        self.layoutVP2.addLayout(self.layoutHAvatarP2)
        self.layoutVP2.addLayout(self.layoutHBombeP2)
        self.boxP2.setLayout(self.layoutVP2)

        self.layoutHBox.addWidget(self.boxP1)
        self.layoutHBox.addWidget(self.boxP2)

        self.mainLayoutV.addLayout(self.layoutHBox)
        self.mainLayoutV.addWidget(self.backQP)
        self.mainLayoutV.addWidget(self.DemarrerPartieQP)
        self.setLayout(self.mainLayoutV)

    def setConnection(self):
        self.PVPQP.clicked.connect(self.onPVP)
        self.PVEQP.clicked.connect(self.onPVE)
        self.Map1QP.clicked.connect(self.onMap1)
        self.Map2QP.clicked.connect(self.onMap2)
        self.Map3QP.clicked.connect(self.onMap3)

        self.avatarP1RedQP.clicked.connect(self.onAvatarP1Red)
        self.avatarP1BlueQP.clicked.connect(self.onAvatarP1Blue)
        self.avatarP1GreenQP.clicked.connect(self.onAvatarP1Green)
        self.TNTP1QP.clicked.connect(self.onP1TNT)
        self.dynamiteP1QP.clicked.connect(self.onP1Dynamite)
        self.bombeHP1QP.clicked.connect(self.onP1BombeH)

        self.avatarP2RedQP.clicked.connect(self.onAvatarP1Red)
        self.avatarP2BlueQP.clicked.connect(self.onAvatarP1Blue)
        self.avatarP2GreenQP.clicked.connect(self.onAvatarP1Green)
        self.TNTP2QP.clicked.connect(self.onP2TNT)
        self.dynamiteP2QP.clicked.connect(self.onP2Dynamite)
        self.bombeHP2QP.clicked.connect(self.onP2BombeH)

        self.backQP.clicked.connect(self.backBouton)
        self.DemarrerPartieQP.clicked.connect(self.onPlay)
        self.DemarrerPartieQP.setDisabled(1)

    def onPVP(self):
        self.PVPQP.setStyleSheet(" font-weight: bold 30px ;  border-style: outset ; color : brown")
        self.PVEQP.setDisabled(1)
        self.status += 1
        self.controller.setModeGame("PvP")
        self.check_status()

    def onPVE(self):
        self.PVEQP.setStyleSheet(" font-weight: bold 30px ;  border-style: outset ; color : brown")
        self.PVPQP.setDisabled(1)
        self.status += 1
        self.controller.setModeGame("PvE")
        self.check_status()

    def onAvatarP1Red(self):
        self.avatarP1RedQP.setStyleSheet(" font-weight: bold 30px ;  border-style: outset ; color : pink")
        self.avatarP1BlueQP.setDisabled(1)
        self.avatarP1GreenQP.setDisabled(1)
        self.status += 1
        Avatar = 'A1'
        self.controller.setAvatar(Avatar, 1)
        self.check_status()

    def onAvatarP1Blue(self):
        self.avatarP1BlueQP.setStyleSheet(" font-weight: bold 30px ;  border-style: outset ; color : pink")
        self.avatarP1RedQP.setDisabled(1)
        self.avatarP1GreenQP.setDisabled(1)
        self.status += 1
        Avatar = 'A2'
        self.controller.setAvatar(Avatar, 1)
        self.check_status()

    def onAvatarP1Green(self):
        self.avatarP1GreenQP.setStyleSheet(" font-weight: bold 30px ;  border-style: outset ; color : pink")
        self.avatarP1RedQP.setDisabled(1)
        self.avatarP1BlueQP.setDisabled(1)
        self.status += 1
        Avatar = 'A3'
        self.controller.setAvatar(Avatar, 1)
        self.check_status()

    def onAvatarP2Red(self):
        self.avatarP2RedQP.setStyleSheet(" font-weight: bold 30px ;  border-style: outset ; color : pink")
        self.avatarP2BlueQP.setDisabled(1)
        self.avatarP2GreenQP.setDisabled(1)
        self.status += 1
        Avatar = 'A1'
        self.controller.setAvatar(Avatar, 2)
        self.check_status()

    def onAvatarP2Blue(self):
        self.avatarP2BlueQP.setStyleSheet(" font-weight: bold 30px ;  border-style: outset ; color : pink")
        self.avatarP2RedQP.setDisabled(1)
        self.avatarP2GreenQP.setDisabled(1)
        self.status += 1
        Avatar = 'A2'
        self.controller.setAvatar(Avatar, 2)
        self.check_status()

    def onAvatarP2Green(self):
        self.avatarP2GreenQP.setStyleSheet(" font-weight: bold 30px ;  border-style: outset ; color : pink")
        self.avatarP2RedQP.setDisabled(1)
        self.bavatarP2BlueQP.setDisabled(1)
        self.status += 1
        Avatar = 'A3'
        self.controller.setAvatar(Avatar, 2)
        self.check_status()

    def onMap1(self):
        self.Map1QP .setStyleSheet(" font-weight: bold 30px ;  border-style: outset ; color : pink")
        self.Map2QP .setDisabled(1)
        self.Map3QP .setDisabled(1)
        self.status += 1
        Map = '../Maps/map1.map'
        self.controller.setMap(Map)
        self.check_status()

    def onMap2(self):
        self.Map2QP .setStyleSheet(" font-weight: bold 30px ;  border-style: outset ; color : pink")
        self.Map1QP .setDisabled(1)
        self.Map3QP .setDisabled(1)
        self.status += 1
        Map = '../Maps/map2.map'
        self.controller.setMap(Map)
        self.check_status()

    def onMap3(self):
        self.Map3QP .setStyleSheet(" font-weight: bold 30px ;  border-style: outset ; color : pink")
        self.Map1QP .setDisabled(1)
        self.Map2QP .setDisabled(1)
        self.status += 1
        Map = '../Maps/map3.map'
        self.controller.setMap(Map)
        self.check_status()

    def onMapUnknow(self):
        self.Map2QP .setStyleSheet(" font-weight: bold 30px ;  border-style: outset ; color : pink")
        self.Map1QP .setDisabled(1)
        self.Map3QP .setDisabled(1)
        self.status += 1
        Map = '../Maps/map2.map'
        self.controller.setMap(Map)
        self.check_status()

    def onP1TNT(self):
        self.TNTQP .setStyleSheet(" font-weight: bold 30px ;  border-style: outset ; color : pink")
        self.dynamiteQP .setDisabled(1)
        self.bombeHQP .setDisabled(1)
        self.status += 1
        Bombe = 'TNT'
        self.controller.setBombe(Bombe)
        self.check_status()

    def onP1Dynamite(self):
        self.dynamiteP1QP .setStyleSheet(" font-weight: bold 30px ;  border-style: outset ; color : pink")
        self.TNTP1QP .setDisabled(1)
        self.bombeHP1QP .setDisabled(1)
        self.status += 1
        Bombe = 'Dynamite'
        self.controller.setBombe(Bombe, 1)
        self.check_status()

    def onP1BombeH(self):
        self.bombeHP1QP .setStyleSheet(" font-weight: bold 30px ;  border-style: outset ; color : pink")
        self.TNTP1QP .setDisabled(1)
        self.dynamiteP1QP .setDisabled(1)
        self.status += 1
        Bombe = 'BombeH'
        self.controller.setBombe(Bombe, 1)
        self.check_status()

    def onP2TNT(self):
        self.TNTP2QP .setStyleSheet(" font-weight: bold 30px ;  border-style: outset ; color : pink")
        self.dynamiteP2QP .setDisabled(1)
        self.bombeP2HQP .setDisabled(1)
        self.status += 1
        Bombe = 'TNT'
        self.controller.setBombe(Bombe, 2)
        self.check_status()

    def onP2Dynamite(self):
        self.dynamiteP2QP .setStyleSheet(" font-weight: bold 30px ;  border-style: outset ; color : pink")
        self.TNTP2QP .setDisabled(1)
        self.bombeHP2QP .setDisabled(1)
        self.status += 1
        Bombe = 'Dynamite'
        self.controller.setBombe(Bombe, 2)
        self.check_status()

    def onP2BombeH(self):
        self.bombeHP2QP .setStyleSheet(" font-weight: bold 150px ;  border-style: outset ; color : pink")
        self.TNTP2QP .setDisabled(1)
        self.dynamiteP2QP .setDisabled(1)
        self.status += 1
        Bombe = 'BombeH'
        self.controller.setBombe(Bombe, 2)
        self.check_status()

    def backBouton(self):
        self.backQP.clicked.connect(self.parent.back)

    def check_status(self):
        if self.status == 6:
            self.DemarrerPartieQP.setDisabled(0)

    def onPlay(self):
        self.DemarrerPartieQP.clicked.connect(self.parent.jouer)

class ElementsWidget(QWidget):
    def __init__(self,parent, controller):
        super().__init__()
        self.controller = controller

class MapWidget(QWidget):
    def ___init__(self,parent,controller):
        super().__init__()
        self.controller = controller

class JeuWindow(QFrame):
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
    app = QApplication(sys.argv)
    controller = ControllerGui()
    timer = QTimer()
    fenetre = MainWindow(controller, timer)
    music = Multimedia(controller)

    music.playGeneralSound()

    timer.timeout.connect(controller.refresh)
    timer.timeout.connect(music.refresh)
    #timer.timeout.connect(fenetre.refresh)



    ##        palette = QPalette()
    ##        palette.setBrush(QPalette.Background,QBrush(QPixmap("../image/bomberman_explosion.png")))
    ##        fenetre.setPalette(palette)
    ##        fenetre.setFixedSize(352,224)
    fenetre.show()
    app.exec()


if __name__ == '__main__':
    main()
