class Produit: 

    def __init__(self, nom, prixHT, TVA): 
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA /100 

    def CalculerPrixTTC(self):
        prixTTC = round(self.prixHT * (1 + self.TVA), 2)
        return prixTTC

    def afficher(self):
        info_produit = (f"nom: {self.nom}, prix HT: {self.prixHT} €, TVA: {self.TVA * 100} %")
        return info_produit

    def modifier_nom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifier_prix(self, nouveau_prix):
        self.prixHT = nouveau_prix

    def retour_nom(self):
        return self.nom

    def retour_prix(self):
        return self.prixHT

    def retour_TVA(self):
        return self.TVA


produit1 = Produit("Bières", 12, 20)
produit2 = Produit("Chips", 2.9, 5.5)
produit3 = Produit("Billetconcert", 60, 2.1)

print(produit1.afficher())
print("Prix TTC pour Bières:", produit1.CalculerPrixTTC())
print(produit2.afficher())
print("Prix TTC pour Chips:", produit2.CalculerPrixTTC())
print(produit3.afficher())
print("Prix TTC pour Billetconcert:", produit3.CalculerPrixTTC())

produit1.modifier_prix(13.5)
produit2.modifier_prix(3.5)
produit3.modifier_prix(65)

print("Modification tarif:", produit1.afficher())
print("Nouveau prix TTC", produit1.CalculerPrixTTC())
print("Modification tarif:", produit2.afficher())
print("Nouveau prix TTC", produit2.CalculerPrixTTC())
print("Modification tarif:", produit3.afficher())
print("Nouveau prix TTC", produit3.CalculerPrixTTC())