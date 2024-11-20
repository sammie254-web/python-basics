# inheritance
# error handling
# dates
from datetime import datetime, date


class Employee:
    def __init__(self, name, id_number, dob, gender):
        self.name = name
        self.id_number = id_number
        self.dob = dob
        self.gender = gender
        date_of_birth = datetime.strptime(dob, '%Y-%m-%d')
        self.age = date.today().year - date_of_birth.year

    def print_details(self):
        print(f'name:{self.name}\nID: {self.id_number}\nDOB: {self.dob}\nGender:{self.gender}\nAge:{self.age}')


# the  child class that is  inheritance
# \nID.....is used to when you want to print each value in its line
class PermanentEmployee(Employee):
    def __init__(self, name, id_number, dob, gender, salary):
        super().__init__(name, id_number, dob,
                         gender)  # instead of repeating the inherited elements use the keyword super
        self.salary = salary

    def print_details(self):
        super().print_details()
        print(f"salary is {self.salary}")


# second inherited class
class TemporaryEmployee(Employee):
    def __init__(self, name, id_number, dob, gender, hourly_pay, end_date):
        super().__init__(name, id_number, dob, gender)
        self.hourly_pay = hourly_pay
        self.end_date = end_date

    def print_hourly_pay(self):
        print(f"hourly payment is{self.hourly_pay}")

    def print_end_date(self):
        print(f"end date is {self.end_date}")


p1 = PermanentEmployee(salary=10000, name='james', id_number='40814234', dob='2006-03-27', gender='male')
p1.print_details()

p2 = TemporaryEmployee(name="mary", id_number="40815213", dob="2003-04-29", gender="female", hourly_pay=10000,
                       end_date="2024-03-27")
p2.print_details()
p2.print_hourly_pay()
p2.print_end_date()
