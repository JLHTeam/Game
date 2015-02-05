import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

app=QApplication([])


class Controller:
        def __init__(self):
                self.message ='Hi! '
                
        def setAvatar(self, Avatar):
                self.Avatar = Avatar
        
        def setMap(self, Map):
                self.Map = Map

        def setBombe(self, bombe):
                self.bombe = bombe

