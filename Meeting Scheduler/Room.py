class Room:
    def __init__(self,name, meet=None):
        self.name = name
        self.isBooked = False
        
        self.meeting = meet
    
    def book(self):
        self.isBooked = True
        print("Room: ",self.name," Booked for: ", self.meeting.getStartTime(), " to: ", self.meeting.getEndTime())
        return self.name
    
    def getBookingStatus(self):
        return "BOOKED" if self.isBooked else "VACANT" 
    
    def getName(self):
        return self.name
    
    def setMeeting(self, meet):
        self.meeting = meet
