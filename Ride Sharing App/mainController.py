from User import User

user1 = User("Sahil","CUSTOMER")

user1.bookRide(50,60,1)
user1.close()

user1.bookRide(50,60,2)

user1.modify(50,70,3)
user1.close()


user1.bookRide(10,20,1)
user1.cancel()
user1.bookRide(10,25,2)
user1.close()


