


class Bombe:
	""" Classe m�re Bombe qui va permettre de cr�e les differents types de mur """
	def __init__(self):
		self._power = 50 #Puissance de l'explosion
		self._TBE = 3000  #Time before explosion (ms)
	
	""" Fonction permettant d'activer le compte � rebours pour explosion """
	def activate(self):
		pass

class BlueBombe(Bombe):
	""" Classe Bombe bleue """
	def __init__(self):
		pass

class GreenBombe(Bombe):
	""" Classe Bombre verte """
	def __init__(self):
		pass
		
class RedBombe(Bombe):
	""" Classe Bombe Rouge puissante """
	def __init__(self):
		self._power = 80 #Puissance de l'explosion

class BlackBombe(Bombe):
	""" Classe Bombe noir les plus puissante et explose tr�s rapidement """
	def __init__(self):
		self._power = 100 #Puissance de l'explosion
		self._TBE = 2000  #Time before explosion
	