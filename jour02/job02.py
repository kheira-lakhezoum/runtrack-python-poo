class Livre: 
    
    def __init__(self, titre, auteur, nbpages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nbpages = nbpages

    def get_titre(self):
        return self.__titre
    
    def set_titre(self, titre):
        self.__titre = titre

    def get_auteur(self):
        return self.__auteur
    
    def set_auteur(self, auteur):
        self.__auteur = auteur

    def get_nbpages(self):
        return self.__nbpages
    
    def set_nbpages(self, nbpages):
        if nbpages > 0 and type(nbpages) == int:
            self.__nbpages = nbpages
        else:
            print("Erreur")

livre = Livre("titre", "auteur", 240)
print(livre.get_nbpages())

livre.set_nbpages(480)
print(livre.get_nbpages())

livre.set_nbpages(546.5)
print(livre.get_nbpages())