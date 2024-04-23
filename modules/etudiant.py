class Etudiant:

    def __init__(self, idetud, nom, prenom, classe):
        self.idetud = idetud
        self.nom = nom
        self.prenom = prenom
        self.classe = classe


    def consulter_planning(self, idPanning):
        print("Voir planning")
