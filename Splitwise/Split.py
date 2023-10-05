class Split:
    def __init__(self):
        pass

    def equalSplit(self, amount, users):
        split = amount // len(users)

        for i in users:
            users.addOwed(split)
    
    def exactSplit(self,amount, users, splitArr):
        for i in range(len(users)):
            users[i].addOwed(splitArr[i])

    def percentageSplit(self,amount, users, splitArr):
        for i in range(len(users)):
            users[i].addOwed(amount*splitArr[i])
    



