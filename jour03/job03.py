class Tache:

    def __init__(self, titre, description, statut="à faire"):
        self.titre = titre
        self.description = description
        self.statut = statut

    def marquerCommeFinie(self):
        self.statut = "terminée"


class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)
        print(f"Tâche '{tache.titre}' ajoutée à la liste.")

    def supprimerTache(self, tache):
        if tache in self.taches:
            self.taches.remove(tache)
            print(f"Tâche '{tache.titre}' supprimée de la liste.")
        else:
            print("La tâche n'existe pas dans la liste.")

    def afficherListe(self):
        print("Liste des tâches :")
        for tache in self.taches:
            print(f"{tache.titre} - {tache.description} - Statut : {tache.statut}")

    def filter_liste(self, statut):
        taches_filtrees = [tache for tache in self.taches if tache.statut == statut]
        return taches_filtrees


# Exemple d'utilisation :
tache1 = Tache("Aller à Carrefour", "Acheter du fromage à raclette")
tache2 = Tache("Faire des exos Python", "et encore des exos Python")
tache3 = Tache("Prendre rdv au spa", "Soin Hermès")

liste_taches = ListeDeTaches()

# Ajout de tâches à la liste
liste_taches.ajouterTache(tache1)
liste_taches.ajouterTache(tache2)
liste_taches.ajouterTache(tache3)

# Affichage de la liste
liste_taches.afficherListe()

# Suppression d'une tâche
liste_taches.supprimerTache(tache2)

# Marquer une tâche comme terminée
tache1.marquerCommeFinie()

# Affichage de la liste mise à jour
liste_taches.afficherListe()

# Filtrer les tâches à faire
taches_a_faire = liste_taches.filter_liste("à faire")
print("\nTâches à faire :")
for tache in taches_a_faire:
    print(f"{tache.titre} - {tache.description} - Statut : {tache.statut}")
