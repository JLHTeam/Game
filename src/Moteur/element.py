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



def testElement():
    elem = Element((0,0))
    bbmb = Bombe(elem.position, 'TNT')
    print(bbmb.power)

if __name__=='__main__':
    testElement()


