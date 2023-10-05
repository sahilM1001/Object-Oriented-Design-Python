from Task import Task
from Sprint import Sprint
class User:
    def __init__(self, name) -> None:
        self.userTasks = []
        self.name = name 
        self.sprints = []

    def createSprint(self,name,start,end):
        sprint = Sprint(name,start,end)
        self.sprints.append(sprint)

    
    def createTask(self,taskType,status,taskName, desc=None):
        newTask = Task(self,taskType,status,taskName)
        self.userTasks.append(newTask)

    
    def changeStatus(self, taskName, stat):
        for i in self.userTasks:
             if i.getName() == taskName:
                 i.setStatus(stat)

        

    
    def addToSprint(self,spr,taskName):
        flag = False
        for i in self.sprints:
            if i.getName() == spr:
                print("sprint ", spr," found")
                flag = True
                for j in self.userTasks:
                    if j.getName() == taskName:
                        i.addTask(j)
        if flag == False:
            print("No Sprint named: ", spr, "was found, please create sprint first and then assign a task to the sprint")
            for i in self.userTasks:
                if i.getName() == taskName:
                    self.userTasks.remove(i)

        

    def removeFromSprint(self,sprintName,taskName):
        for i in self.sprints:
            if i.getName() == sprintName:
                for j in i.getTasks():
                    if j.getName() == taskName:
                        i.setTasks(i.getTasks().remove(j))


    def printTasks(self):
        for i in self.userTasks:
            print("Task Name: ",i.getName())
            print("Task status: ", i.getStatus())

    def printSprintTask(self, sprintName):
        for i in self.sprints:
            if i.getName() == sprintName:
                print(i.getTasks())


        
                        


