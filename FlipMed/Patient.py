class Patient:
    counter = 0
    def __init__(self, name) -> None:
        self.id=self.get_unique_id()
        self.name = name
        self.bookings = {}

    def get_name(self):
        return self.name
    
    def get_unique_id(self):
        Patient.counter += 1
        return Patient.counter
    
    def get_bookings(self):
        return self.bookings
    
    def show_bookings(self):
        for key, val in self.bookings.items():
            print("You have a booking between : ", key, " with Doctor: ", val.get_name(), " for specialty: ", val.get_specialty())

    def add_booking(self, slot, doctor):
        if slot not in self.get_bookings():
            self.bookings[slot] = doctor
            return True
        else:
            print("You cannot book for the same slot again")
            return False

    def cancel_booking(self, slot):
        flag = False
        for key, val in self.get_bookings():
            if key == slot:
                flag = True
                val.set_availability(slot)

        if flag:
            print("Your slot booking was cancelled successfully")
        else:
            print("No slot booking found, cannot cancel booking")
            



