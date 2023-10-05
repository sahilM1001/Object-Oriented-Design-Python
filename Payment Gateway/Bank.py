class Bank:
    def __init__(self, bankName, support):
        self.name = bankName
        self.support = support.split(" ")
    def runTransaction(self):
        from random import randint
        return randint(0,1)
