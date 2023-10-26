from FlipMed import FlipMed
from Doctor import Doctor
from Patient import Patient



d1 = Doctor("A","Gastrology")
d2 = Doctor("B",  "Cardiology")
d3 = Doctor("C", "Gastrology")

d1.set_availability("9:30AM-10:00AM")
d1.set_availability("10:30AM-11:00AM")
d1.set_availability("4:30PM-5:00PM")

d2.set_availability("9:30AM-10:00AM")
d2.set_availability("10:30AM-11:00AM")
d2.set_availability("4:30PM-5:00PM")


d3.set_availability("11:30AM-12:00PM")
d3.set_availability("10:30AM-11:00AM")
d3.set_availability("5:30PM-6:00PM")

booking_system = FlipMed()

booking_system.register_doctor(d1)
booking_system.register_doctor(d2)
booking_system.register_doctor(d3)

booking_system.show_specialities()

booking_system.show_all_slots("Gastrology")

p1 = Patient("X")
p2 = Patient("y")

booking_system.register_patient(p1)
booking_system.register_patient(p2)

booking_system.book_slot("9:30AM-10:00AM", p1,d1)

d1.show_bookings()

p1.show_bookings()

print(booking_system.all_bookings)



