from Splitwise import Splitwise
from User import User
from Expense import Expense

u1 = User("Sahil")
u2 = User("B")
u3 = User("C")

split_wise_main = Splitwise()

split_wise_main.register_user(u1)
split_wise_main.register_user(u2)
split_wise_main.register_user(u3)

print(split_wise_main.user_ids)

exp1 = Expense("Food",u1,"EXACT", [u2, u3], 1000,None,[200,500])

split_wise_main.add_expense(exp1)

split_wise_main.print_balance_for_users()

print(u1.user_expense_sheet)

exp2 = Expense("Item 2",u2,"EQUAL",[u1, u3],300)

split_wise_main.add_expense(exp2)

split_wise_main.print_balance_for_users()
