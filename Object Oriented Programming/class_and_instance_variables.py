class Hospital:
    hospital_name = "City Care Hospital"
    patient_count = 0

    def __init__(self, name, room):
        self.name = name
        self.room = room
        Hospital.patient_count += 1

    def show_patient(self):
        print("Hospital:", Hospital.hospital_name)
        print("Patient:", self.name)
        print("Room Number:", self.room)

p1 = Hospital("Anil", 101)
p2 = Hospital("Meera", 205)

p1.show_patient()
print()
p2.show_patient()
print("Total Patients:", Hospital.patient_count)
