class FlipMed:
    def __init__(self) -> None:
        self.doctors = []
        self.patients = []
        self.all_bookings = {}
        self.specialities = set()

    def show_all_slots(self, specialty):
        for i in self.doctors:
            if i.get_specialty() == specialty:
                availability = i.get_availability()

                for key, val in availability.items():
                    if val == "Available":
                        print("Dr ", i.get_name(), " is available at slot : ", key, " for specialty : ", specialty)
    
    def register_doctor(self, doctor):
        self.doctors.append(doctor)
        if doctor.get_specialty() not in self.specialities:
            self.specialities.add(doctor.get_specialty())

    def show_specialities(self):
        print("Specialities available")
        for i in self.specialities:
            print(i)

    def register_patient(self, patient):
        self.patients.append(patient)

    def book_slot(self, slot, patient, doctor):
        ret = doctor.book_slot(slot, patient)
        if ret == True:
            patient_ret = patient.add_booking(slot, doctor)
            if patient_ret == True:
                tmp = {
                    'patient': patient,
                    'doctor':  doctor
                }
                if slot not in self.all_bookings:
                    self.all_bookings[slot] = [tmp]
                else:
                    self.all_bookings[slot].append(tmp)

            print("Confirmed booking for : ", patient.get_name(), " with doctor: ", doctor.get_name(), " for slot: ", slot)

    def cancel_slot_booking(self, slot, patient):
        patient.cancel_booking(slot)
        
        

