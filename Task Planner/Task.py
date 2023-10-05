class Task:
    def __init__(self,user,taskType,status,taskName,desc=None):
        self.user = user 
        self.taskType = taskType
        self.taskStatus = status
        
        self.taskName = taskName
    
    def setStatus(self,status):
        self.taskStatus = status

    def setTaskType(self,type1):
        self.taskType = type1

    def getStatus(self):
        return self.taskStatus

    def setUser(self,user):
        self.user = user

    def getUser(self):
        return self.user   

    def getName(self):
        return self.taskName   
  