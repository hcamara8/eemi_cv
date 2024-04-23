class Enseignant:

    def __init__(self, idprof, nom, prenom, matiere):
        self.idprof = idprof
        self.nom = nom
        self.prenom = prenom
        self.matiere = matiere

    def faire_reservation(self, idSalle, debut, fin):
        print("réalise la reservation")

    def consulter_planning(self, idPanning):
        print("Voir planning")

        
