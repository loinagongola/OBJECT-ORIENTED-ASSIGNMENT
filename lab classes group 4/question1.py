class Student:
    def __init__(self, name, id_number, address):
        self.name = name
        self.id_number = id_number
        self.address = address

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.id_number}")
        print(f"Address: {self.address}")

student = Student("Mako", "N2134", "123 Main St,calgary")
student.display_info()
