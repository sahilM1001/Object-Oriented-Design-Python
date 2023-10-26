class Splitwise:
    def __init__(self):
        self.users = []
        self.user_ids = set()

    def add_expense(self, expense):
        """ if self.verify_users(expense.get_credit_user(), expense.get_debit_users()):
            print("Users verified") """
        self.calculate_expenses(expense)

    def register_user(self, user):
        if user.get_user_id() not in self.user_ids:
            self.users.append(user)
            self.user_ids.add(user.get_user_id())

    def verify_users(self,creditor, other_users):
        if creditor.get_user_id() not in self.user_ids:
            return False
        for i in other_users:
            if i.get_user_id() not in self.user_ids:
                return False


    def print_balance_for_users(self):
        for i in self.users:
            i.get_total_expense()
        pass

    def calculate_expenses(self, expense):
        cred = expense.get_credit_user()
        debit_users = expense.get_debit_users()
        total_outstanding = 0
        
        if expense.get_split_type() == "EXACT":
            exact_distributions =expense.get_exact_distribution()

            for i in range(0, len(debit_users)):
                debit_users[i].add_to_user_expense_sheet(debit_users[i],exact_distributions[i])
                total_outstanding += exact_distributions[i]

        elif expense.get_split_type() == "PERCENT":
            
            percent_distributions =expense.get_percent_distribution()
            
            for i in range(0, len(debit_users)):
                debit_users[i].add_to_user_expense_sheet(debit_users[i],percent_distributions[i] * expense.get_total_amount()) 
                total_outstanding += (percent_distributions[i] * expense.get_total_amount())

        else:
            print("Equal split")
            total_amount = expense.get_total_amount()
            share_per_user = total_amount / len(debit_users)
            
            for i in range(0, len(debit_users)):
                debit_users[i].add_to_user_expense_sheet(debit_users[i],share_per_user)

                total_outstanding += share_per_user
        cred.set_total_outstanding(total_outstanding)

        

                
