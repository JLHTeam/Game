


class Wall:
	""" Classe m�re Wall qui va permettre de cr�e les differents types de mur """
	def __init__(self):
		self._health = 100
		self._isDestructible = None
	
	""" Fonction permettant de d�truire le mur """
	def destroy(self):
		pass
	
	
class DWall(Wall):
	""" Classe m�re Wall Destructible """
	def __init__(self):
		self._isDestructible = True
	
	""" Fonction permettant de d�truire le mur """
	def destroy(self):
		pass
		
class NDWall(Wall):
	""" Classe m�re Wall qui va permettre de cr�e les differents types de mur """
	def __init__(self):
		self._isDestructible = False
	
	""" Fonction permettant de d�truire le mur petit � petit """
	def destroy(self):
		pass