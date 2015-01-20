

class Case:

    def __init__(self,position='(1,1)'):
        self.sorte=None
        self.position=position      # tuple de coordonées

    def __repr__(self):
        c=self.sorte
        return c

class Mur(Case):

    def __init__ (self,parent):  #,position="(1,1)"):????
        super().__init__(parent)
        self.niveau_vie_supplémentaire=0
        self.position=None                        # tuple de ces coordonées dans la matrice
        self.sorte=3+self.niveau_vie_supplémentaire



class Vide:

    def __init__(self):
        pass

    def __repr__(self):
        v=0
        return v


class Carte:

    def __init__(self,liste_murs=None,dimension=(30,30)):
        self.liste_lignes=[]
        self.liste_colonnes=[]
        self.matrice=[]
        self.liste_murs=liste_murs
        self.dimension=dimension         # tuple de coordonnées

    def creation(self):
        for case in range(int(self.dimension[0])):
                self.liste_lignes.append(Case())
        for case in range(int(self.dimension[1])):
                self.liste_colonnes.append(Case())
        for ligne in self.liste_lignes:
                #for colonne in self.liste_colonnes:
                     self.matrice.append(self.liste_colonnes)


    def remplissage(self):
        for mur in self.liste_murs:
              for ligne in self.liste_lignes:
                  for colonne in self.liste_colonnes:
                        if (mur.position)==(ligne,colonne):
                                  Case(mur.position).sorte=mur

        for case in self.liste_colonnes:
            if case.sorte==None:
                 case.sorte=Vide()



def test_carte():

    mur_1=Mur(Case)
    mur_2=Mur(Case)
    mur_3=Mur(Case)
    mur_1.position=(1,1)
    mur_2.position=(5,8)
    mur_3.position=(7,2)
    mur_1.niveau_vie_supplémentaire=1
    liste=[mur_1, mur_2, mur_3]
    carte=Carte(liste,(10,10))
    carte.creation()
    carte.remplissage()
    print(carte)



if __name__=='__main__':
    test_carte()




