class Ride:
    def __init__(self, origin, destination, seats) -> None:
        import random
        self.id = random.randint(0,9)
        self.origin = origin
        self.destination = destination
        self.seats = seats
        self.pricePerKM = 20
        self.charges = 0
        self.distance = self.destination - self.origin
        self.status = ""
    def getSeats(self):
        return self.seats
    def setSeats(self,seats):
        self.seats = seats
    def getStatus(self):
        return self.status
    def setStatus(self,status):
        self.status = status
    def getOrigin(self):
        return self.origin
    def setOrigin(self, origin):
        self.origin = origin
    def getDestination(self):
        return self.destination
    def setDestination(self,destination):
        self.destination = destination
    def setDistance(self, distance):
        self.distance = distance
    def getDistance(self):
        return self.distance
    def setCharges(self, charges):
        self.charges = charges
    def getCharges(self):
        return self.charges

