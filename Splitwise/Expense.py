from Split import Split

class Expense:
    def __init__(self, description, amount):
        self.description = description
        self.amount = amount
        
    def split(self, type, users, splitArr=None):
        splitFunc = Split()
        if type == "EXACT":
            splitFunc.exactSplit(self.amount, users, splitArr)
        elif type == "EQUAL":
            splitFunc.equalSplit(self.amount, users)
        else:
            splitFunc.percentageSplit(self.amount, users, splitArr)
        

