class Student: 
    
    def __init__(self, nom, prenom, numetudiants, credits):
        self.__nom = nom
        self.__prenom = prenom
        self.__numetudiants = numetudiants
        self.__credits = 0
        self.__level = self.__studentEval()

    def add_credits(self, n):
        if n > 0:
            self.__credits += n 

    def get_nom(self):
        return self.__nom

    def set_nom(self, nom):
        self.__nom = nom

    def get_prenom(self):
        return self.__prenom

    def set_nom(self, prenom):
        self.__prenom = prenom

    def get_numetudiants(self):
        return self.__numetudiants

    def set_nom(self, numetudiants):
        self.__numetudiants = numetudiants

    def get_credits(self):
        return self.__credits

    def set_credits(self, n):
        self.__credits = n 

    def __studentEval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    
etudiant = Student("John", "Doe", 145, 0)
print(etudiant.get_nom(), etudiant.get_prenom(), etudiant.get_numetudiants())

print("Crédit initial : ",etudiant.get_credits())

etudiant.add_credits(10)
print("Crédité de 10 :", "total",etudiant.get_credits())

etudiant.add_credits(5)
print("Crédité de 5 :", "total",etudiant.get_credits())

etudiant.add_credits(20)
print("Crédité de 20 :", "total",etudiant.get_credits())

print("Niveau:", etudiant._Student__level) 
