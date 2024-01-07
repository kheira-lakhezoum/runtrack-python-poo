class Joueur:

    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts_marques = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0

    def marquerUnBut(self):
        self.buts_marques += 1

    def effectuerUnePasseDecisive(self):
        self.passes_decisives += 1

    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1

    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1

    def afficherStatistiques(self):
        print(f"Statistiques de {self.nom} (#{self.numero}, {self.position}):")
        print(f"Buts marqués: {self.buts_marques}")
        print(f"Passes décisives: {self.passes_decisives}")
        print(f"Cartons jaunes: {self.cartons_jaunes}")
        print(f"Cartons rouges: {self.cartons_rouges}")
        print("")

class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []

    def ajouterJoueur(self, joueur):
        self.joueurs.append(joueur)

    def afficherStatistiquesJoueurs(self):
        print(f"Statistiques des joueurs de l'équipe {self.nom}:")
        for joueur in self.joueurs:
            joueur.afficherStatistiques()

    def MAJStatistiquesJoueur(self, nom_joueur, buts=0, passes=0, jaunes=0, rouges=0):
        for joueur in self.joueurs:
            if joueur.nom == nom_joueur:
                joueur.buts_marques += buts
                joueur.passes_decisives += passes
                joueur.cartons_jaunes += jaunes
                joueur.cartons_rouges += rouges
                break

equipe1 = Equipe("Équipe de France")
equipe2 = Equipe("Équipe d'Argentine")

joueur1 = Joueur("MBappé", 10, "Attaquant")
joueur2 = Joueur("Messi", 10, "Attaquant")

equipe1.ajouterJoueur(joueur1)
equipe2.ajouterJoueur(joueur2)


equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()


joueur1.marquerUnBut()
joueur2.effectuerUnePasseDecisive()


equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()
