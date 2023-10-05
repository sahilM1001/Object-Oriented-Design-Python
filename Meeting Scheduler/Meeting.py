class Meeting:
    def __init__(self,startTime, endTime,name):
        self.startTime = startTime
        self.endTime = endTime
        self.roomName= name


    def setStartTime(self, startTime):
        self.startTime = startTime
    def getStartTime(self):
        return self.startTime
    
    def setEndTime(self, endTime):
        self.endTime = endTime
    def getEndTime(self):
        return self.endTime
    
    def setRoomName(self, room):
        self.roomName = room
    def getRoomName(self):
        return self.roomName
