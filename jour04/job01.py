class Personne: 

    def __init__(self):
        self.age = 14

    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age 
    
    def afficherAge(self):
        print(self.get_age())

    def bonjour(self):
        print("Hello")

    def modifierAge(self, age):
        self.set_age(age)

class Eleve(Personne):

    def __init__(self):
        Personne.__init__(self)

    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print(f"J'ai {self.get_age()} ans")

class Professeur:

    def __init__(self, matiereEnseignee):
        self.__matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")

    
eleve = Eleve()
eleve.afficherAge()

personne = Personne()

     