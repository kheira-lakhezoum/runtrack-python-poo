class Rectangle:

    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur
    
    def set_longueur(self, longueur):
        self.__longueur = longueur

    def get_largeur(self):
        return self.__largeur
    
    def set_largeur(self, largeur):
        self.__largeur = largeur
    
    def perimetre(self):
        return (self.__longueur + self.__largeur) * 2
    
    def surface(self):
        return self.__longueur * self.__largeur
    
class Parallelepipede(Rectangle):

    def __init__(self, hauteur,longueur,largeur):
        Rectangle.__init__(self,longueur,largeur)
        self.hauteur = hauteur

    def get_hauteur(self):
        return self.hauteur
    
    def set_hauteur(self, hauteur):
        self.hauteur = hauteur

    def volume(self):
        return self.get_longueur() * self.get_largeur() * self.hauteur 
    
parallelepipede = Parallelepipede(10,5,8)
print(parallelepipede.volume())
