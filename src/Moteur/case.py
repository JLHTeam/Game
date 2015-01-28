import sys

class Case:
    def __init__(self, sorte = 0):
        self.sorte = sorte
        self.health = 0
        if sorte == 1:
            self.health = pow(2,32)
        if sorte == 2:
            self.health = 100

    def hurt(self, degat):
        self.health = max(self.health - degat, 0)
        if self.health == 0:
            self.sorte == 0

    def __repr__(self):
        return str(self.sorte)

def testCase():
    _case = Case(15)


if __name__=='__main__':
    testCase()