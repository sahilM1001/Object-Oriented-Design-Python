from Room import Room
from Meeting import Meeting
class Scheduler:
    def __init__(self):
        self.rooms = []
        for i in range(5):
            self.rooms.append(Room("Room_"+str(i)))
        
    def showRooms(self):
        for i in self.rooms:
            if i.getBookingStatus() != "BOOKED":
                print("Room: ", i.getName(),  " is available for booking")

    def book(self, start,end):
        
        bookingFlag = False
        for i in self.rooms:
            
            if i.getBookingStatus() == "VACANT":
                bookingFlag = True
                i.setMeeting(Meeting(start,end, i.getName()))
                i.book()
                return i.getName()
        if bookingFlag == False:
            return "Sorry no rooms are available to book"

        
