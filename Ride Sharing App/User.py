from Ride import Ride
class User:
    def __init__(self, name, userType):
        self.name = name
        self.USER_TYPE = userType
        self.ride=None

    def bookRide(self,origin, destination, seats):
        if self.USER_TYPE == "CUSTOMER":
            self.ride = Ride(origin, destination, seats)

            print("Ride from : ", self.ride.getOrigin(), " to : ", self.ride.getDestination(), " booked for : ", self.ride.getSeats(), " seats")
            self.ride.setStatus("BOOKED")
        else:
            print("Only customers can book a ride")
        
    def cancel(self):
        self.ride.setStatus("CANCELLED") 

    def modify(self, origin=None, destination=None, seats=None):
        if origin is not None:
            self.ride.setOrigin(origin) 
        if destination is not None:
            self.ride.setDestination(destination)
        if seats is not None:
            self.ride.setSeats(seats) 
        print("Ride modified from : ", self.ride.getOrigin(), " to : ", self.ride.getDestination(), " booked for : ", self.ride.getSeats(), " seats")
        

    def close(self):
        print(self.ride.getDistance())
        self.ride.setDistance(self.ride.getDestination()- self.ride.getOrigin()) 
        if self.ride.getSeats() >= 2:
            
            self.ride.setCharges(self.ride.getDistance() * self.ride.getSeats() * 0.75 * self.ride.pricePerKM)
        else:
            self.ride.setCharges(self.ride.getDistance() * self.ride.pricePerKM) 
        self.ride.setStatus("COMPLETED") 
        print("Ride complete, please pay: ", self.ride.getCharges())





