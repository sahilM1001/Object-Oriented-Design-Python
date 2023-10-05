class Sprint:
    def __init__(self, name,beginDate,endDate):
        self.sprintName = name
        self.beginDate = beginDate
        self.endDate = endDate
        self.tasks = []
    def getName(self):
        return self.sprintName
    
    def addTask(self,task):
        self.tasks.append(task)

    def getTasks(self):
        return self.tasks
    def setTasks(self, tasks):
        self.tasks = tasks
    
    def printTasks(self):
        for i in self.tasks:
            print("Task Name: ", i.getName())
            print("Task assigned to: ", i.getUser())

    