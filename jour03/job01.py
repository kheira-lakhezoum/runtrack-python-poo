class Ville:

    def __init__(self, nom, nbhabitants):
        self.__nom = nom
        self.__nbhabitants = nbhabitants

    def get_nbhabitants(self):
        return self.__nbhabitants
    
    def set_nbhabitants(self, nbhabitants):
        self.__nbhabitants = nbhabitants

class Personne: 

    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville

    def ajouterPopulation(self, ville):
        ajouter = ville.get_nbhabitants()+1
        ville.set_nbhabitants(ajouter)
    
ville_Paris = Ville ("Paris", 1000000)
ville_Marseille = Ville ("Marseille", 861635)

print ("Population marseillaise :", ville_Marseille.get_nbhabitants())
print ("Population parisienne :", ville_Paris.get_nbhabitants())
    
John = Personne ("John", 45, ville_Paris)
Myrtille = Personne ("Myrtille", 4, ville_Paris)
Chloé = Personne ("Chloé", 18, ville_Marseille)

John.ajouterPopulation(ville_Paris)
Myrtille.ajouterPopulation(ville_Paris)
Chloé.ajouterPopulation(ville_Marseille)

print("Nouvelle population marseillaise :", ville_Marseille.get_nbhabitants())
print("Nouvelle population parisienne :", ville_Paris.get_nbhabitants())
