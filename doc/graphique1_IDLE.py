import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
 
app=QApplication([])


#class MonWidgetDessin(QGraphicsView): def __init__(self, parent):
#super().__init__(parent) self.setScene(self.dessiner())
#def dessiner(self):
#scene = QGraphicsScene()
#scene.setSceneRect(0, 0, 300, 300)
#texte = scene.addText("Hellimport sys

#class MonWidgetDessin(QGraphicsView): def __init__(self, parent):
#super().__init__(parent) self.setScene(self.dessiner())
#def dessiner(self):
#scene = QGraphicsScene()
#scene.setSceneRect(0, 0, 300, 300)
#texte = scene.addText("Hello, world!") texte.setPos(10,10)
#scene.addLine(50, 50, 200, 200)
#stylo = QPen(Qt.blue, 5, Qt.SolidLine) scene.addEllipse(200,100,20,20, stylo)
#brosse = QBrush(QColor(128,0,128), Qt.SolidPattern) scene.addRect(100,200,50,50, stylo, brosse)
#return scene

class Controller:
        def __init__(self):
                pass

class Jeu_Window(QMainWindow):
        def __init__(self,controller):
                super().__init__()
                self.setWindowTitle('BomberMan JLHTeam')
                
        
class Boutons(QWidget):
            def __init__(self,parent, controller):
                 super().__init__()
                 self.controller = controller
                 
class Avatar(QWidget):
            def __init__(self,parent, controller):
                 super().__init__()
                 self.controller = controller
        
        def main():
        app=QApplication(sys.argv)
        controller = Controller()
        fenetre= Jeu_Window(controller)
        fenetre.show()
        app.exec()


if __name__ == '__main__':
    main()
