import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def __str__(self):
        return f"{self.valeur} de {self.couleur}"

class Jeu:
    def __init__(self):
        valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        couleurs = ['Coeur', 'Carreau', 'Trèfle', 'Pique']
        self.paquet = [Carte(valeur, couleur) for valeur in valeurs for couleur in couleurs]
        random.shuffle(self.paquet)

    def calculer_points(self, main):
        points = 0
        as_count = 0

        for carte in main:
            if carte.valeur.isdigit():
                points += int(carte.valeur)
            elif carte.valeur in ['J', 'Q', 'K']:
                points += 10
            elif carte.valeur == 'A':
                as_count += 1

        for i in range(as_count):
            if points + 11 <= 21:
                points += 11
            else:
                points += 1

        return points

    def jouer(self):
        main_joueur = [self.paquet.pop(), self.paquet.pop()]
        main_croupier = [self.paquet.pop(), self.paquet.pop()]

        while True:
            print(f"\nMain du joueur : {[str(carte) for carte in main_joueur]} - Points : {self.calculer_points(main_joueur)}")
            print(f"Carte du croupier : {str(main_croupier[0])}")

            choix = input("Voulez-vous prendre une carte (A) ou passer (P) ? ").upper()

            if choix == 'P':
                main_joueur.append(self.paquet.pop())
                if self.calculer_points(main_joueur) > 21:
                    print(f"\nMain du joueur : {[str(carte) for carte in main_joueur]} - Points : {self.calculer_points(main_joueur)}")
                    print("Vous avez dépassé 21. Vous avez perdu!")
                    return
            elif choix == 'P':
                break

        while self.calculer_points(main_croupier) < 17:
            main_croupier.append(self.paquet.pop())

        print(f"\nMain du joueur : {[str(carte) for carte in main_joueur]} - Points : {self.calculer_points(main_joueur)}")
        print(f"Main du croupier : {[str(carte) for carte in main_croupier]} - Points : {self.calculer_points(main_croupier)}")

        if self.calculer_points(main_joueur) > self.calculer_points(main_croupier) and self.calculer_points(main_joueur) <= 21:
            print("Vous avez gagné!")
        elif self.calculer_points(main_croupier) <= 21:
            print("Le croupier a gagné!")
        else:
            print("Le croupier a dépassé 21. Vous avez gagné!")

jeu_blackjack = Jeu()
jeu_blackjack.jouer()
