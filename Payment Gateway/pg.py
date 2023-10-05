from Clients import Clients
from Bank import Bank

class paymentGateway:
    
    def __init__(self):
        self.clients = {}
        self.transactions = []
        
    def addClient(self, clientName):
        #function to create new client in the payment gateway
        c1 = Clients(clientName)
        self.clients[clientName] = c1
    def showClients(self):
        print("==============================================")
        print("Clients of the Payment Gateway")
        print("==============================================")
        print(self.clients.keys())
        print("==============================================")
        print("self.clients: ", self.clients)
        
    def removeClient(self, clientName):
        #function ot remove client from the payment gateway
        del self.clients[clientName]
        
    def listSupportedPayModesClient(self, clientName):
        temp = self.clients[clientName]
        temp.listSupportedPayModes()
    def addSupportedPayModesClient(self, clientName,pyMode):
        temp = self.clients[clientName]
        temp.addSupportForPayModes(pyMode)
    def removePayModeForClient1(self, clientName, pyMode):
        temp = self.clients[clientName]
        temp.removePayModeForClient(pyMode)

    def makePayment(self,details):
        #function to perform payments
        pType = details['type']
        if pType == "UPI":
            temp = {
                "pType": "UPI",
                "for_client": details['client_name'],
                "amount": details['amount'],
                "bank_name": "SBI"
            }
            
            if details['client_name'] in self.clients.keys() and pType in self.clients[details['client_name']].paymentModes:
                bankName = Bank("SBI", "UPI")
                status = bankName.runTransaction()
                details['bank_name'] = bankName.name
                details['temp'] = temp
                if status == 1:
                    self.UPITransaction(details)
                else:
                    print("Transaction failed due to bank issue")
                
            else:
                print("Transaction Could not be completed because client name was invalid")

        if pType == "Netbanking":
            temp = {
                "pType": "Netbanking",
                "for_client": details['client_name'],
                "amount": details['amount'],
                "bank_name": "HDFC"
            }
            
            if details['client_name'] in self.clients.keys() and pType in self.clients[details['client_name']].paymentModes:
                bankName = Bank("HDFC", "Netbanking")
                status = bankName.runTransaction()
                details['bank_name'] = bankName.name
                details['temp'] = temp
                if status == 1:
                    self.netBankingTransaction(details)
                else:
                    print("Transaction failed due to bank issue")
            else:
                print("Transaction Could not be completed because client name or payment mode was invalid")
    
    def UPITransaction(self, details):
        if 'upi_pin' in details.keys():
            self.clients[details['client_name']].addAmount(details['amount'])
            print("---------------------------------------")
            print("UPI Transaction of amount ", details['amount'], " performed by ", details['bank_name'], " for client ", details['client_name'])
            print("---------------------------------------")

            print("===========================================")
            print("Updated balance of client ", details['client_name'], " is : ", self.clients[details['client_name']].balanceAmount())
            print("===========================================")
            self.transactions.append(details['temp'])
        else:
            print("TRANSACTION FAILED DUE TO INCORRECT DETAILS SUPPLIED TO UPI Transaction")

    def netBankingTransaction(self, details):
        if 'user_id' in details.keys() and 'password' in details.keys():
            self.clients[details['client_name']].addAmount(details['amount'])
            print("---------------------------------------")
            print("Netbanking Transaction of amount ", details['amount'], " performed by ", details['bank_name'], " for client ", details['client_name'])
            print("---------------------------------------")

            print("===========================================")
            print("Updated balance of client ", details['client_name'], " is : ", self.clients[details['client_name']].balanceAmount())
            print("===========================================")
            self.transactions.append(details['temp'])
        else:
            print("INCORRECT DETAILS SUPPLIED TO Netbanking Transaction")

    def viewTransactions(self):
        if len(self.transactions) > 0:
            for i in self.transactions:
                print("--------------------------------------------")
                print(i)
                print("--------------------------------------------")
        else:
            print("No transactions are performed on the gateway")

import time
start = time.time()
print("Program execution has started")

pg = paymentGateway()
pg.addClient("Flipkart")
pg.addClient("Amazon")
pg.showClients()

import sys


pg.addSupportedPayModesClient("Flipkart","UPI")
pg.addSupportedPayModesClient("Amazon","Netbanking")
pg.addSupportedPayModesClient("Amazon","UPI")
pg.listSupportedPayModesClient("Flipkart")
pg.listSupportedPayModesClient("Amazon")

details = {
    'type': 'UPI',
    'client_name': 'Flipkart',
    'amount': 120,
    'upi_pin': 1231
}

pg.makePayment(details)

details1 = {
    'type': 'UPI',
    'client_name': 'Flipkart',
    'amount': 1300
}
pg.makePayment(details1)

details2 = {
    'type': 'Netbanking',
    'client_name': 'Flipkart',
    'amount': 12,
    'user_id': "sahil1",
    'password': 'sahil123'
}
pg.makePayment(details2)

details3 = {
    'type': 'UPI',
    'client_name': 'Amazon',
    'amount': 2000
}
pg.makePayment(details3)

details4 = {
    'type': 'Netbanking',
    'client_name': 'Amazon',
    'amount': 100,
    'password': 'sahil123'
}
pg.makePayment(details4)

pg.viewTransactions()

print("==========================================================")
print("Program Execution took: ", (time.time() - start))
print("==========================================================")
