class User:
    counter = 0
    def __init__(self, name):
        self.name = name
        self.id = self.get_unique_id()
        self.user_expense_sheet = []
        self.total_expense = 0
        self.total_outstanding = 0

    def get_unique_id(self):
        User.counter +=1
        return User.counter
    
    def add_to_user_expense_sheet(self, user, amount):
    
        self.total_expense += amount    
        #self.total_outstanding -= amount
    
        for i in self.user_expense_sheet:
            if i[0].get_user_id() == self.get_user_id():
                i[1] += amount
                break
        self.user_expense_sheet.append([user,amount])

    def get_total_expense(self):
        if self.total_expense > 0 and self.total_outstanding > 0:
            print(self.name, " owes :", self.total_expense, " to other users AND gets back : ", self.total_outstanding, " from other users")
        elif self.total_expense > 0:
            print(self.name, " owes :", self.total_expense, " to other users")
        else:
            print(self.name, " gets back : ", self.total_outstanding, " from other users")
        

    def get_user_id(self):
        return self.id

    def get_user_name(self):
        return self.name
    
    def get_total_outstanding(self):
        return self.get_total_outstanding

    def set_total_outstanding(self, value):
        self.total_outstanding += value

    

