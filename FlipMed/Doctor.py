class Doctor:
    counter = 0
    def __init__(self, name, specialty):
        self.id = self.get_unique_id()
        self.name = name
        self.specialty = specialty
        self.availability = {}

    def get_unique_id(self):
        Doctor.counter += 1
        return Doctor.counter
    
    def get_name(self):
        return self.name

    def set_name(self, value):
        self.name = value

    def get_specialty(self):
        return self.specialty

    def set_specialty(self, value):
        self.specialty = value

    def get_availability(self):
        return self.availability

    def set_availability(self,key):
        if key not in self.availability:
            self.availability[key] = "Available"
        else:
            self.availability[key] = "Available"

    def show_bookings(self):
        for key,val in self.availability.items():
            if val != "Available":
                print("You have a booking for slot: ", key)

    def book_slot(self, slot, patient):
        if self.availability[slot] == "Available":
            self.availability[slot] = patient
            return True
        else:
            print("Doctor ", self.name, " is unavailable for the slot: ", slot)
            return False
    
