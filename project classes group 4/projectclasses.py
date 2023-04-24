class Doctor:
    def __init__(self, doctor_id, name, specialization, working_time, qualification, room_number):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.working_time = working_time
        self.qualification = qualification
        self.room_number = room_number
    
    # getter method
    def get_doctor_id(self):
        return self.doctor_id
    def get_name(self):
        return self.name
    def get_specialization(self):
        return self.specialization
    def get_working_time(self):
        return self.working_time
    def get_qualification(self):
        return self.qualification
    def get_room_number(self):
        return self.room_number
    
    # setter method
    def set_doctor_id(self, sec_doctor_id):
        self.doctor_id = sec_doctor_id
    def set_name(self, sec_name):
        self.name = sec_name
    def set_specialization(self, sec_specialization):
        self.specialization = sec_specialization
    def set_working_time(self, sec_working_time):
        self.working_time = sec_working_time
    def set_qualification(self, sec_qualification):
        self.sec_qualification = sec_qualification 
    def set_room_number(self, sec_room_number):
        self.sec_room_number = sec_room_number
    # return strings
      
        

class DoctorManager:
    def __init__(self):
        self.doctors_list = []
    def format_dr_info(self, doctor_id, name, specialization, working_time, qualification, room_number):
        doctor_id = input("enter the doctors id: ")
        name = input("enter the doctors name: ")
        specialization = input("enter the doctors specialization: ")
        working_time = input("enter the doctors working time: ")
        qualification = input("enter the doctors qualification: ") 
        room_number = input("enter the doctors room number: ")
        
    f = open(__file__, "r'")
        
        

class Patient: 
    def __init__(self, patient_id, name, disease,gender, age):
        self.patient_id = patient_id
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age
    
    #getter method
    def get_patient_id(self):
        return self.patient_id
    def get_name(self):
        return self.name
    def get_disease(self):
        return self.disease
    def get_gender(self):
        return self.gender
    def get_age(self):
        return self.age
    
    #setter method
    def set_patient_id(self, sec_patient_id):
        self.sec_patient_id = sec_patient_id
    def set_name(self, sec_name):
        self.sec_name = sec_name
    def set_disease(self, sec_disease):
        self.sec_disease = sec_disease
    def set_gender(self, sec_gender):
        self.sec_gender = sec_gender
    def set_age(self, sec_age):
        self.sec_age = sec_age
    
    # returning strings

class PatientManager:

class Management:
