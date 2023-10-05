from users import User

wallets = {}
transactionStore = []
accounts = []
def transferFunction():
    wallet1 = input("Enter Wallet 1: ")
    wallet2 = input("Enter Wallet 2: ")
    amt = input("Enter Amount to transfer: ")
    if (wallets[wallet1].checkBalance() > int(amt)) and (wallet2 in wallets.keys()):
        #check for offer 1:
        
        wallets[wallet1].transferAmount(int(amt))
        wallets[wallet2].receiveAmount(int(amt))
        if wallets[wallet1].checkBalance() == wallets[wallet2].checkBalance():
            applyOffer1(wallet1,wallet2)
    else:
        print("Either wallet balance was less than transfer amount or receiving wallet was not found")
    temp = {
        'wallet_from': wallet1,
        'wallet_to': wallet2,
        'amount': amt
        }
    balanceUpdater(wallet1, wallet2)
    transactionStore.append(temp)

def applyOffer1(wallet1,wallet2):
    wallets[wallet1].receiveAmount(10)
    wallets[wallet2].receiveAmount(10)
    temp = {
        'wallet_from': wallet1,
        'wallet_to': wallet2,
        'amount': 10
    }
    balanceUpdater(wallet1,wallet2)
    transactionStore.append(temp)

def balanceUpdater(wallet1, wallet2):
    for i in accounts:
        print("i: ", i)
        if i['user_name'] == wallet1:
            i['balance'] = wallets[wallet1].checkBalance()
        if i['user_name'] == wallet2:
            i['balance'] = wallets[wallet2].checkBalance()

def transactionPrinter():
    inp1 = input("Enter username to check account statement: ")
    if len(transactionStore)> 0:
        for i in transactionStore:
            if i['wallet_from'] == inp1 or i['wallet_to'] == inp1:
                print("----------------------------------------------")
                print("i: ", i)
                print("----------------------------------------------")
                print("Transaction From: ", i['wallet_from'])
                print("Transaction To: ", i['wallet_to'])
                print("Transaction Amount: ", i['amount'])
                print("----------------------------------------------")
        print("Current Balance for ", inp1, " is : ", wallets[inp1].checkBalance())
    else:
        print("No transactions are performed")

def accountSummary():
    if len(wallets) > 0:
        print("wallets: ", wallets)
        for i in wallets: 
            print("----------------------------------------------")
            print("Account name: ", wallets[i].name)
            print("Current Balance: ", wallets[i].checkBalance())
            print("----------------------------------------------")
    else:
        print("No transactions are performed")

def startingFunc():
    inp = 0 
    while inp != 5:
        inp = int(input("Enter 1 to create account and provide a starting balance \nEnter 2 to transfer money between two accounts \nEnter 3 for account statement \nEnter 4 to view summary of all accounts\nEnter 5 to exit: "))
        if inp == 1:
            inp1 = input("Enter username for the account and starting balance: ")

            user = User(inp1.split(" ")[0], int(inp1.split(" ")[1]))
            wallets[user.name] = user
            accounts.append({'user_name': user.name, 'balance':int(inp1.split(" ")[1])})
            print("accounts: ", accounts)
        if inp == 2:
            #function to perform wallet transfer
            transferFunction()
        if inp == 3:
            #show account statement for the user
            transactionPrinter()
        if inp == 4:
            #view all transactions:
            accountSummary()
startingFunc()