class Clients:
    def __init__(self,clientName):
        self.clientName = clientName
        self.paymentModes = []
        self.balance = 0
    def listSupportedPayModes(self):
        #function to show payment modes supported by a client
        print("Payment modes supported by ", self.clientName, " are : ", self.paymentModes)
        
    def addSupportForPayModes(self, mode):
        #function to add payment modes to a client
        self.paymentModes.append(mode)
        print("Payment mode ", mode, " added to client: ", self.clientName)

    def removePayModeForClient(self,mode):
        #function to remove payment modes from a client
        self.paymentModes.remove(self.paymentModes.index(mode))
        print("Payment mode ", mode, " removed from client: ", self.clientName)

    def addAmount(self, amount):
        self.balance += amount
    
    def balanceAmount(self):
        return self.balance
