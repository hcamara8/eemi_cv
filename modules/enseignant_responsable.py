from enseignant import Enseignant


class EnseignatResponsable(Enseignant):

    def __init__(self, idprof, nom, prenom, matiere):
        super().__init__(idprof, nom, prenom, matiere)
        self.pouvoir_edition = True


    def modifier_recapitulatif(self, idRecap):
        print("Modification de l'ID du récaputilatif")


    