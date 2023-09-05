class Doctor:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization

class Department:
    def __init__(self, name):
        self.name = name
        self.doctors = []

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Appointment:
    def __init__(self, patient, department, doctor, reason, date_time):
        self.patient = patient
        self.department = department
        self.doctor = doctor
        self.reason = reason
        self.date_time = date_time

# Create Department objects and attach doctors
dept_cardiology = Department("Cardiology")
dept_cardiology.add_doctor(Doctor("Dr. J Ramlingam", "Cardiologist"))
dept_cardiology.add_doctor(Doctor("Dr. KK Sharma", "Cardiologist"))

dept_orthopedics = Department("Orthopedics")
dept_orthopedics.add_doctor(Doctor("Dr. P Krishna", "Orthopedic Surgeon"))
dept_orthopedics.add_doctor(Doctor("Dr. Deepak", "Orthopedic Surgeon"))

# Sample patient
patient_name = input("Enter patient name: ")
patient_age = int(input("Enter patient age: "))
patient = Patient(patient_name, patient_age)

while True:
    print("\nAvailable Departments:")
    print("1. Cardiology")
    print("2. Orthopedics")
    department_choice = input("Select a department (1/2): ")

    if department_choice == '1':
        selected_department = dept_cardiology
    elif department_choice == '2':
        selected_department = dept_orthopedics
    else:
        print("Invalid department choice.")
        continue

    print("\nDoctors in", selected_department.name)
    for index, doctor in enumerate(selected_department.doctors, start=1):
        print(f"{index}. {doctor.name} - {doctor.specialization}")

    doctor_choice = int(input("Select a doctor (1/2): ")) - 1

    if 0 <= doctor_choice < len(selected_department.doctors):
        selected_doctor = selected_department.doctors[doctor_choice]
    else:
        print("Invalid doctor choice.")
        continue

    appointment_reason = input("Enter reason for the appointment: ")
    appointment_date_time = input("Enter date and time of the appointment: ")

    appointment = Appointment(patient, selected_department, selected_doctor, appointment_reason, appointment_date_time)

    print("Hospital Appointment Program -- Taruvar Singhal E22CSEU1454")
    print("\nAppointment Details:")
    print("Patient:", appointment.patient.name)
    print("Department:", appointment.department.name)
    print("Doctor:", appointment.doctor.name)
    print("Reason:", appointment.reason)
    print("Date and Time:", appointment.date_time)
    print("Your appointment has been booked!!!")

    another_appointment = input("Do you want to make another appointment? (yes/no): ")
    if another_appointment.lower() != "yes":
        break

