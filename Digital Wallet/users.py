class User:
    def __init__(self, name, bal):
        self.name = name
        self.balance = bal
        
    def checkBalance(self):
        return self.balance
    def transferAmount(self, amt):
        self.balance -= amt
    def receiveAmount(self, amt):
        self.balance += amt
