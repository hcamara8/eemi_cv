from reservation import Reservation


class ReservationMateriels(Reservation):

    def __init__(self,  idReservation, date):
        super().__init__( idReservation, date)
        self.type = "MATERIELS"
        self.expiration = 4