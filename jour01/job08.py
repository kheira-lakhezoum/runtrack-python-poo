import math 

class Cercle: 

    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self, nouveauRayon):
        self.rayon = nouveauRayon

    def circonference(self):
        return 2* self.rayon * math.pi
    
    def air(self):
        return math.pi * self.rayon ** 2 
    
    def diametre(self):
        return self.rayon * 2
    
    def afficherInfos(self):
        print(f"le rayon est de {self.rayon}, la circonference est de {self.circonference()}, l'air est de {self.air()}, le diametre est de {self.diametre()}")
    
cercle1 = Cercle(4)
cercle1.afficherInfos()

cercle2 = Cercle(7)
cercle2.afficherInfos()

