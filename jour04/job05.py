import math 

class Forme: 

    def __init__(self):
        pass

    def aire(self):
        return 0


class Rectangle(Forme):

    def __init__(self, largeur, hauteur):
        Forme.__init__(self)
        self.__largeur = largeur
        self.__hauteur = hauteur
        
    def get_largeur(self):
        return self.__largeur
    
    def set_largeur(self, largeur):
        self.__largeur = largeur
    
    def get_hauteur(self):
        return self.__hauteur
    
    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur

    def aire(self):
        return self.__hauteur * self.__largeur


class Cercle(Forme):

    def __init__(self, radius):
        Forme.__init__(self)
        self.radius = radius

    def get_radius(self):
        return self.radius
    
    def set_radius(self, radius):
        self.radius = radius

    def aire(self):
        return math.pi * self.radius**2
    

rectangle = Rectangle(5,10)
print(rectangle.aire())

cercle = Cercle(15)
print(cercle.aire())
