class CompteBancaire:

    def __init__(self, numero_compte, nom, prenom, solde_initial, decouvert=False):
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde_initial
        self.__decouvert = decouvert

    def afficher(self):
        print(f"Compte #{self.__numero_compte} - {self.__prenom} {self.__nom}")

    def afficher_solde(self):
        print(f"Solde actuel : {self.__solde} €")

    def versement(self, montant):
        self.__solde += montant
        print(f"Versement de {montant} € effectué. Nouveau solde : {self.__solde} €")

    def retrait(self, montant):
        if self.__solde - montant >= 0 or self.__decouvert:
            self.__solde -= montant
            print(f"Retrait de {montant} € effectué. Nouveau solde : {self.__solde} €")
        else:
            print("Opération impossible. Solde insuffisant.")

    def agios(self, taux):
        if self.__solde < 0:
            agios = abs(self.__solde) * taux
            self.__solde -= agios
            print(f"Agios appliqués : {agios} €. Nouveau solde : {self.__solde} €")

    def virement(self, compte_destinataire, montant):
        if self.__solde - montant >= 0 or self.__decouvert:
            self.__solde -= montant
            compte_destinataire.versement(montant)
            print("Virement effectué avec succès.")
        else:
            print("Opération impossible. Solde insuffisant.")

compte1 = CompteBancaire(1, "Berlin", "B", 1000)
compte2 = CompteBancaire(2, "Le Professor", "P", -500, decouvert=True)

compte1.afficher()
compte1.afficher_solde()

compte1.versement(200)
compte1.afficher_solde()

compte1.retrait(300)
compte1.agios(0.02)

compte2.afficher()
compte2.afficher_solde()

compte1.virement(compte2, 150)
compte1.afficher_solde()

compte2.afficher_solde()

compte1.virement(compte2, 850)
compte1.afficher()
compte1.afficher_solde()
compte2.afficher()
compte2.afficher_solde()
