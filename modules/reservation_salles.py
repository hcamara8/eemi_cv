from reservation import Reservation


class ReservationSalles(Reservation):

    def __init__(self,  idReservation, date):
        super().__init__( idReservation, date)
        self.type = "SALLES"
        self.adresse = "Adresse de la salle"

