from User import User
from Sprint import Sprint
from Task import Task

u1 = User("sahil")
u1.createSprint("SPRINT 1",1,2)
u1.createTask("FEATURE","STARTED",taskName="task1")

u1.addToSprint("SPRINT 1","task1")
#u1.printTasks()

u1.removeFromSprint("SPRINT 1","task1")

u1.printTasks()

u1.printSprintTask("SPRINT 1")


