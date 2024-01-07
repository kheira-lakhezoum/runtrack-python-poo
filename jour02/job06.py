class Commande:
    
    def __init__(self, numCommande):
        self.__numCommande = numCommande
        self.__platsCommandes = {} 
        self.__statutCommande = "en cours"

    def ajouter_plat(self, nomPlat, prixPlat):
        if nomPlat not in self.__platsCommandes:
            self.__platsCommandes[nomPlat] = {"prix": prixPlat, "statut": "en cours"}
            print(f"Plat '{nomPlat}' ajouté à la commande.")
        else:
            print(f"Plat '{nomPlat}' déjà en commande.")

    def annuler_commande(self):
        self.__platsCommandes = {}
        self.__statutCommande = "annulée"
        print("La commande a été annulée.")

    def __calculer_total(self):
        total = sum(plat["prix"] for plat in self.__platsCommandes.values())
        return total

    def afficher_commande(self):
        print(f"Commande #{self.__numCommande} - Statut : {self.__statutCommande}")
        for nom_plat, plat in self.__platsCommandes.items():
            print(f"{nom_plat} - {plat['prix']} € - Statut : {plat['statut']}")
        print("Total à payer:", self.__calculer_total(), "€")

    def calculer_tva(self):
        tva = self.__calculer_total() * 0.2  
        return tva

commande = Commande(1)

commande.ajouter_plat("Pizza 3 fromages", 12.5)
commande.ajouter_plat("Pizza Peperronni", 10.5)
commande.ajouter_plat("Pizza chevre_miel ", 11.5)

commande.afficher_commande()

tva = commande.calculer_tva()
print("TVA à payer:", tva, "€")

commande.annuler_commande()
commande.afficher_commande()
