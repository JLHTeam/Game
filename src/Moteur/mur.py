


class Wall:
	""" Classe mère Wall qui va permettre de crée les differents types de mur """
	def __init__(self):
		self._health = 100
		self._isDestructible = None
	
	""" Fonction permettant de détruire le mur """
	def destroy(self):
		pass
	
	
class DWall(Wall):
	""" Classe mère Wall Destructible """
	def __init__(self):
		self._isDestructible = True
	
	""" Fonction permettant de détruire le mur """
	def destroy(self):
		pass
		
class NDWall(Wall):
	""" Classe mère Wall qui va permettre de crée les differents types de mur """
	def __init__(self):
		self._isDestructible = False
	
	""" Fonction permettant de détruire le mur petit à petit """
	def destroy(self):
		pass