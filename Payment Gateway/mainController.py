from pg import paymentGateway

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
