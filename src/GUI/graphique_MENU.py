import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import graphique_ETAT_DEMARRAGE_PARTIE

app=QApplication([])


class JeuWindow(QMainWindow):
        def __init__(self,controller):
                super().__init__()
                self.setWindowTitle('BomberMan JLHTeam_Menu')
                controller.definir_fenetre_principale(self)
                menu_widget = Menu_Widget(self, controller)
                self.setCentralWidget(menu_widget)
                
        def change_widget(self, widget):
                self.setCentralWidget(widget)

                
class Controller:
        def __init__(self):
                self.message ='Hi! '

        def definir_fenetre_principale(self,widget):
                self.fenetre=widget


        def on_ouvrir_1(self):
                demarrer_widget = Demarrer_Widget(self.fenetre,self)
                self.fenetre.change_widget(demarrer_widget)

        def on_ouvrir_2(self):
#Faire choisir parmi des configuration puis stocker les elments 
##                jeu_widget = Jeu_Widget(self.fenetre,self)
##                self.fenetre.change_widget(jeu_widget)
                pass
                

        def back(self):
                menu_widget = Menu_Widget(self.fenetre,self)
                self.fenetre.change_widget(menu_widget)

        def jouer(self):
                jeu_widget = Jeu_Widget(self.fenetre,self)
                self.fenetre.change_widget(jeu_widget)
                
        def setAvatar(self, Avatar):
                self.Avatar=Avatar
        
        def setMap(self, Map):
                self.Map=Map

        


class Menu_Widget(QFrame):
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
                 self.setStyleSheet("Menu_Widget{background-image: url(./image/bomberman_explosion.png); color:white}")
                 image = QPixmap("./image/bomberman_explosion.png")
                 size = image.width()
                 parent.setFixedSize(352,224)

class Demarrer_Widget(QFrame):
            def __init__(self,parent, controller):
                 super().__init__()
                 self.controller = controller
                 layoutV = QVBoxLayout()
 #                texte = QLabel('DEMARRAGE PARTIE')
 #                texte.setStyleSheet("color : yellow; font-weight: bold")
                 self.zone_texte=QTextEdit(controller.message)
 #                self.zone_texte.setReadOnly(True)
                 #self.zone_texte.setStyleSheet("background-image: url(./image/Neo Bomberman-acouper.png); color:white")
                 self.zone_texte.setAlignment(Qt.AlignHCenter)
 #                self.zone_texte.setStyleSheet("QTextEdit {color:white}")
 #                layoutV.addWidget(WidgetDessin(self,controller))
                 #2 lignes à enlever qd resolue image en fond et non devant..!!!
                 layoutH = QHBoxLayout()
                 layoutH2 = QHBoxLayout()
                 self.bouton1 = QPushButton('Joueur VS Joueur',self)
                 self.bouton2 = QPushButton('Joueur VS Ordinateur',self)
                 self.bouton3 = QPushButton('Revenir à l’écran d’accueil',self) 
                 self.bouton4 = QPushButton(' Map 1 ',self)
                 self.bouton5 = QPushButton('Map 2',self)
                 self.bouton6 = QPushButton('Map 3',self)
                 self.bouton2 .setStyleSheet("border : None ; font-weight: bold 30px") #que le tour:  border-style: outset 
                 self.bouton1 .setStyleSheet("border : None ; font-weight: bold 30px")
                 self.bouton3 .setStyleSheet("border : None ; font-weight: bold 30px")
                 self.bouton4 .setStyleSheet("border : None ; font-weight: bold 30px")
                 self.bouton5 .setStyleSheet("border : None ; font-weight: bold 30px")
                 self.bouton6 .setStyleSheet("border : None ; font-weight: bold 30px")
                 layoutH.addWidget(self.bouton1)
                 layoutH.addWidget(self.bouton2)
                 layoutV.addLayout(layoutH)
                 indication = QLabel('Choisir la Map')
                 layoutH2.addWidget(indication)
                 layoutH2.addWidget(self.bouton4)
                 layoutH2.addWidget(self.bouton5)
                 layoutH2.addWidget(self.bouton6)
                 layoutV.addLayout(layoutH2)
                 layoutH3 = QHBoxLayout()
                 indication2 = QLabel('Choisir un Joueur')
                 self.bouton7 = QPushButton('Avatar 1',self)
                 self.bouton8 = QPushButton('Avatar 2',self)
                 self.bouton9 = QPushButton('Avatar 3',self)
                 self.bouton7 .setStyleSheet("border : None ; font-weight: bold 30px")
                 self.bouton8 .setStyleSheet("border : None ; font-weight: bold 30px")
                 self.bouton9 .setStyleSheet("border : None ; font-weight: bold 30px")
                 layoutH3.addWidget(indication2)
                 layoutH3.addWidget(self.bouton7)
                 layoutH3.addWidget(self.bouton8)
                 layoutH3.addWidget(self.bouton9)
                 layoutV.addLayout(layoutH3)
                 self.bouton1.clicked.connect(self.on_selection1)
                 self.bouton2.clicked.connect(self.on_selection2)
                 self.bouton4.clicked.connect(self.on_selection4)
                 self.bouton5.clicked.connect(self.on_selection5)
                 self.bouton6.clicked.connect(self.on_selection6)
                 self.bouton7.clicked.connect(self.on_selection7)
                 self.bouton8.clicked.connect(self.on_selection8)
                 self.bouton9.clicked.connect(self.on_selection9)
                 
                 layoutV.addWidget(self.bouton3)
                 self.bouton3.clicked.connect(self.back_bouton)
                 self.bouton10 = QPushButton('Démarrer la Partie',self)
                 layoutV.addWidget(self.bouton10)
                 self.bouton10.clicked.connect(self.on_jouer)
                 self.bouton10.setDisabled(1)
#                 layoutV.addWidget(texte)
  #               layoutV.addWidget(self.zone_texte)
                 self.setStyleSheet("Demarrer_Widget{background-image: url(./image/Bomberman.jpg); color:white}")
                 self.setLayout(layoutV)
                 parent.setFixedSize(350,250)
                 #self.zone_texte.show()
                 self.status=0


            def on_selection1(self):
                self.bouton1.setStyleSheet(" font-weight: bold 30px ;  border-style: outset ; color : brown")
                self.bouton2.setDisabled(1)
                self.status+=1;
                self.check_status()

            def on_selection2(self):
                self.bouton2.setStyleSheet(" font-weight: bold 30px ;  border-style: outset ; color : brown")
                self.bouton1.setDisabled(1)
                self.status+=1;
                self.check_status()

            def on_selection7(self):
                self.bouton7.setStyleSheet(" font-weight: bold 30px ;  border-style: outset ; color : pink")
                self.bouton8.setDisabled(1)
                self.bouton9.setDisabled(1)
                self.status+=1;
                Avatar='A1'
                self.controller.setAvatar(Avatar)
                self.check_status()
                
            def on_selection8(self):
                self.bouton8.setStyleSheet(" font-weight: bold 30px ;  border-style: outset ; color : pink")
                self.bouton7.setDisabled(1)
                self.bouton9.setDisabled(1)
                self.status+=1;
                Avatar='A2'
                self.controller.setAvatar(Avatar)
                self.check_status()

            def on_selection9(self):
                self.bouton9.setStyleSheet(" font-weight: bold 30px ;  border-style: outset ; color : pink")
                self.bouton7.setDisabled(1)
                self.bouton8.setDisabled(1)
                self.status+=1;
                Avatar='A3'
                self.controller.setAvatar(Avatar)
                self.check_status()
                

            def on_selection4(self):
                self.bouton4.setStyleSheet(" font-weight: bold 30px ;  border-style: outset ; color : pink")
                self.bouton6.setDisabled(1)
                self.bouton5.setDisabled(1)
                self.status+=1;
                Map='Map1'
                self.controller.setMap(Map)
                self.check_status()
                
            def on_selection5(self):
                self.bouton5.setStyleSheet(" font-weight: bold 30px ;  border-style: outset ; color : pink")
                self.bouton4.setDisabled(1)
                self.bouton6.setDisabled(1)
                Map='Map2'
                self.controller.setMap(Map)
                self.check_status()

            def on_selection6(self):
                self.bouton6.setStyleSheet(" font-weight: bold 30px ;  border-style: outset ; color : pink")
                self.bouton4.setDisabled(1)
                self.bouton5.setDisabled(1)
                self.status+=1;
                Map='Map3'
                self.controller.setMap(Map)
                self.check_status()

            def back_bouton(self):
                 self.connect(self.bouton3,SIGNAL('clicked()'),self.controller.back)

            def check_status(self):
                 if self.status==3:
                    self.bouton10.setDisabled(0)

            def on_jouer(self):
                    self.connect(self.bouton10,SIGNAL('clicked()'),self.controller.jouer)

                    


                
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
                 self.bouton2.clicked.connect(self.on_bouton2)


            def on_bouton1(self):
                 self.connect(self.bouton1,SIGNAL('clicked()'),self.controller.on_ouvrir_1)

            def on_bouton2(self):
                 self.connect(self.bouton2,SIGNAL('clicked()'),self.controller.on_ouvrir_2)




def main():
        app=QApplication(sys.argv)
        controller = Controller()
        fenetre= JeuWindow(controller)
##        palette = QPalette()
##        palette.setBrush(QPalette.Background,QBrush(QPixmap("./image/bomberman_explosion.png")))
##        fenetre.setPalette(palette)
##        fenetre.setFixedSize(352,224)
        fenetre.show()
        app.exec()


if __name__ == '__main__':
    main()
