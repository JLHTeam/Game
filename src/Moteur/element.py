import sys

class Element:
	def __init__(self, position = (1,1)):
		self.position = position



class Bombe(Element):
	"""  """
	def __init__(self, position, sorte):
		super().__init__(position)
		self.sorte = sorte
		self.statut = 0 #0 = desactivé - 1 = waiting - 2 = expolse

		if self.sorte == 'Dynamite':
			self.power = 50 #Puissance de l'explosion
			self.TBE = 2000  #Time before explosion (ms)
			self.porte = 1

		if self.sorte == 'TNT':
			self.power = 100 #Puissance de l'explosion
			self.TBE = 2000  #Time before explosion (ms)
			self.porte = 2

		if self.sorte == 'BombeH':
			self.power = 200 #Puissance de l'explosion
			self.TBE = 3000  #Time before explosion (ms)
			self.porte = 4

	def refresh(self):
		pass


class Joueur(Element):
	def __init__(self, position, sorte):
		super().__init__(position)
		self.sorte = sorte
		self.health = 300

	def refresh(self):
		pass

	def setAction(self): # récupérer action
		pass

	def creerBombe(self):
		pass

	def move(self, commande):
		if commande == 1:
			self.position[0] -= 1
		if commande == 2:
			self.position[0] += 1
		if commande == 3:
			self.position[1] -= 1
		if commande == 4:
			self.position[1] += 1
		commande = 0


class JoueurIA(Joueur):
	def __init__(self):
		super().__init__()

	def refresh(self):
		pass


class JoueurH(Joueur):
	def __init__(self):
		super().__init__()
		self.commande = 0

	def refresh(self): # Evolution temps discret (Timer) du mouvement
		if self.commande == 5:
			self.creerBombe()
		else:
			self.move(self.commande)

	def setAction(self, commande): # Evolution temps réel de commande - buffer commande
		self.commande = commande


def testElement():
	elem = Element((0,0))
	bbmb = Bombe(elem.position, 'TNT')
	print(bbmb.power)

if __name__=='__main__':
	testElement()


