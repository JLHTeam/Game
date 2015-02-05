import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import graphique_ETAT_DEMARRAGE_PARTIE

app=QApplication([])


class Controller:
        def __init__(self):
                self.message ='Hi! '

        def definir_fenetre_principale(self,widget):
                self.fenetre=widget

        def on_ouvrir_1(self):
                demarrer_widget = Demarrer_Widget(self.fenetre,self)
                self.fenetre.change_widget(demarrer_widget)

        def on_charger(self):
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

