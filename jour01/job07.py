class Personnage:

    def __init__ (self, x, y):
        self.x = x
        self.y = y

    def gauche(self):
        self.x -=1
    
    def droite(self):
        self.x +=1

    def bas(self):
        self.y +=1

    def haut(self):
        self.y -=1

    def position(self):
        return (self.x, self.y)
    
personnage = Personnage (0, 15)

personnage.gauche()
personnage.haut()

position = personnage.position()

print(f"Les coordonnées de la position du personnage sont:", position)


