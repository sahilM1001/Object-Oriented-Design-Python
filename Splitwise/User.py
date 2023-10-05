class User:
    def __init__(self,name):
        self.name = name
        self.owed = 0
        self.expense =[]

    def findOwed(self):
        print(self.name, " owes ", self.owed)

    def addOwed(self,amount):
        self.owed+= amount

    
    