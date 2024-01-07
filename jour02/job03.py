class Livre: 
    
    def __init__(self, titre, auteur, nbpages):
        self.__titre = "L'univers"
        self.__auteur = auteur
        self.__nbpages = nbpages
        self.__disponible = True

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

    def verification(self):
        if self.__disponible == True:
            return True
        else:
            return False
    
    def emprunter(self):
        if self.verification():
            self.__disponible = False
            print(f"Le livre '{self.__titre}' a été emprunté.")
        else:
            print(f"Le livre '{self.__titre}' n'est pas disponible.")

    def rendre(self):
        if not self.verification():
            self.__disponible = True
            print(f"Le livre '{self.__titre}' a été rendu avec succès.")
        else:
            print(f"Le livre '{self.__titre}' n'a pas été emprunté, impossible de le rendre.")

livre = Livre("titre", "auteur", 240)
print(livre.get_nbpages())
print("Le livre est disponible:", livre.verification())  

livre.emprunter() 
livre.rendre() 

livre.set_nbpages(480.5)
print(livre.get_nbpages())

