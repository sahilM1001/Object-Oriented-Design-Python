from User import User
from Expense import Expense

u1 = User("Sahil")
u2 = User("Heena")

e1 = Expense("Home", 100)
e1.split("EQUAL",[u2])

print()