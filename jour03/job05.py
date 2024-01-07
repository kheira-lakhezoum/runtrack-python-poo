import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        coups = random.randint(1, 3)
        print(f"{self.nom} attaque {adversaire.nom} et recoit {coups} coups.")
        adversaire.vie -= coups

class Jeu:
    def __init__(self):
        self.niveau = 1

    def choisir_niveau(self):
        try:
            self.niveau = int(input("Choisissez le niveau de difficulté (1, 2 ou 3) : "))
            if self.niveau not in [1, 2, 3]:
                print("Niveau invalide. Le niveau par défaut (1) sera utilisé.")
                self.niveau = 1
        except ValueError:
            print("Entrée invalide. Le niveau par défaut (1) sera utilisé.")

    def lancer_jeu(self):
        print("Bienvenue dans Mortal Combat !")
        self.choisir_niveau()

        joueur = Personnage("Joueur", self.niveau * 3)
        ennemi = Personnage("Ennemi", self.niveau * 3)

        while joueur.vie > 0 and ennemi.vie > 0:
            joueur.attaquer(ennemi)
            if ennemi.vie <= 0:
                print(f"{ennemi.nom} you lose !")
                break

            ennemi.attaquer(joueur)
            if joueur.vie <= 0:
                print(f"{joueur.nom} you lose !")
                break

            print(f"\nStatut actuel :\n{joueur.nom} - Vie : {joueur.vie}\n{ennemi.nom} - Vie : {ennemi.vie}\n")

jeu = Jeu()
jeu.lancer_jeu()
