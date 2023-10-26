class Expense:
    counter = 0
    def __init__(self, description, creditor, split_type, debit_users, total_amount, percent_distribution=None, exact_distribution=None):
        self.id = self.get_unique_id()
        self.description = description
        self.split_type = split_type
        self.percent_distribution = percent_distribution
        self.exact_distribution = exact_distribution
        self.credit_user = creditor
        self.debit_users = debit_users
        self.total_amount = total_amount

    def get_credit_user(self):
        return self.credit_user

    def set_credit_user(self, value):
        self.credit_user = value

    def get_debit_users(self):
        return self.debit_users

    def set_debit_users(self, value):
        self.debit_users = value

    def get_total_amount(self):
        return self.total_amount

    def set_total_amount(self, value):
        self.total_amount = value

    def get_description(self):
        return self.description

    def set_description(self, value):
        self.description = value

    def get_split_type(self):
        return self.split_type

    def set_split_type(self, value):
        self.split_type = value

    def get_percent_distribution(self):
        return self.percent_distribution

    def set_percent_distribution(self, value):
        self.percent_distribution = value

    def get_exact_distribution(self):
        return self.exact_distribution

    def set_exact_distribution(self, value):
        self.exact_distribution = value

    def get_unique_id(self):
        Expense.counter += 1
        return Expense.counter
