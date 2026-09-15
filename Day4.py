#OOPS
#Classes and Objects

import re

class Car:
    wheels = 4

    def __init__(self, distance, time, rc_number, color):
        self.distance = distance
        self.time = time
        self.speed = 0
        self.__rc_number = None  
        self.color = color
        
        try:
            self.set_rc_number(rc_number)
        except ValueError as e:
            print(f"Initialization Alert: {e}")

    def calculate_speed(self) -> float:
        self.speed = self.distance / self.time
        return self.speed
    
    def get_rc_number(self):
        return self.__rc_number

    def set_rc_number(self, new_rc):
        pattern = r"^[A-Z]{2}\d{1,2}[A-Z\d]*-?\d{4}$"
        try:
            if re.match(pattern, new_rc):
                self.__rc_number = new_rc
            else:
                raise ValueError(f"'{new_rc}' does not match the required vehicle registration format.")
        except ValueError as error:
            print(f"Validation Error caught: {error}")

    def describe_vehicle(self):
        return f"A car with {self.wheels} wheels painted with {self.color}"

#Inheritence,Polymorphism,Encapsulation
class Auto(Car):
    def __init__(self, distance, time, passengers, rc_number, color):
        super().__init__(distance, time, rc_number, color)
        self.passengers = passengers
        self.wheels = 3  

    def display_trip_info(self):
        self.calculate_speed()
        return f"You have travelled {self.distance}km in {self.time}hrs with a speed of {self.speed}Km/hr holding {self.passengers} passengers"

    def describe_vehicle(self):
        return f"An auto with {self.wheels} wheels painted with {self.color}"

bad_auto = Auto(10, 1, 2, "INVALID-RC-123", "Red")

auto1 = Auto(25, 1, 3, "MH12-2222", "Yellow")
auto1.set_rc_number("123-ABC")
auto1.set_rc_number("DL3C-9999")
print(f"Current safe RC status: {auto1.get_rc_number()}")


#Abstraction
from abc import ABC, abstractmethod

class Member(ABC):
    university_name = "SRM University"  

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_student_details(self):
        pass
    @classmethod
    def change_university(cls, new_name):
        cls.university_name = new_name
    @staticmethod
    def is_valid_email(email):
        return "@" in email and email.endswith(".edu")

class Student(Member):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id
    def get_student_details(self):
        return f"Student: {self.name} | ID: {self.student_id} | University: {self.university_name}"

email_check = Member.is_valid_email("alex@gtu.edu")
print(f"Is email valid? {email_check}")


student1 = Student("Arjun", "S101")
student2 = Student("Sarah", "S102")

print("Before University Name Change:")
print(student1.get_student_details())
print(student2.get_student_details())

Member.change_university("Metropolitan Innovation University")

print("After University Name Change:")
print(student1.get_student_details())
print(student2.get_student_details())


#Magic Methods and Operator Overloading
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return self.real + other.real, self.imag + other.imag

c1 = Complex(1, 2)
c2 = Complex(2, 3)
print(c1 + c2)