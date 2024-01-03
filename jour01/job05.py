# Créer une classe nommée Point avec les attributs x et y correspondant aux
# coordonnées horizontales et verticales du point. Les deux attributs doivent être
# initialisés dans le constructeur.

# La classe Point doit posséder les méthodes suivantes :

# - afficherLesPoints qui affiche les coordonnées des points.
# - afficherX et afficherY qui affiche respectivement x et y.
# - changerX et changerY qui change la valeur des attributs x et y.

class Point :

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def afficherLesPoints(self):
        print(self.x, self.y)
    
    def afficherX(self):
        print(self.x)

    def afficherY(self):
        print(self.y)

    def changerX(self, x):
        self.x = x

    def changerY(self, y):
        self.y = y
    
point = Point(10, 20)
point.afficherLesPoints()
point.afficherX()
point.afficherY()
point.changerX(24)
point.changerY(42)
point.afficherLesPoints()
        