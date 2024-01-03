class Personne : 
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom 

    def SePresenter(self):
        return (f"je suis {self.prenom} {self.nom}")
    
kheira = Personne ("Lakhezoum", "Kheira")
jennifer = Personne ("K", "Jennifer")
print(kheira.SePresenter())
print(jennifer.SePresenter())