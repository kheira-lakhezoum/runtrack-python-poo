class Vehicule:

    def __init__(self, marque, modele, annee, prix):
        self.marque = marque 
        self.modele = modele
        self.annee = annee
        self.prix = prix 

    def informationsVehicule(self):
        print(self.marque)
        print(self.modele)
        print(self.annee)
        print(self.prix)

    def demarrer(self):
        print("Attention, je roule")


class Voiture(Vehicule):

    def __init__(self, marque, modele, annee, prix):
        Vehicule.__init__(self, marque, modele, annee, prix)
        self.portes = 4
    
    def informationsVehicule(self):
        Vehicule.informationsVehicule(self)
        print(self.portes)

    def demarrer(self):
        print("Demarre mon gros bolide !")

voiture = Voiture("AUDI", "A1", 2023, 24990)
voiture.informationsVehicule()
voiture.demarrer()


class Moto(Vehicule): 

    def __init__(self, marque, modele, annee, prix):
        Vehicule.__init__(self, marque, modele, annee, prix)
        self.roue = 2

    def informationsVehicule(self):
        Vehicule.informationsVehicule(self)
        print(self.roue)

    def demarrer(self):
        print("En Y sur le port !")

moto = Moto("Kawazaki", "Ninja", 2022, 14990)
moto.informationsVehicule()
moto.demarrer()
