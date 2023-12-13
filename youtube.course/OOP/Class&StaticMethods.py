# Example Class
class Employee:
    # class variable
    raise_amount = 1.04
    num_of_emps = 0

    # init method -> constructor
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = str.lower(first) + '.' + str.lower(last) + '@company.com'

    # class method
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Phyton', 'OOP', 50000)
emp_2 = Employee('Test', 'User', 60000)

# Employee.set_raise_amount(1.05)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
#
# emp_str_1 = "Employee-Worker-79876"
#
# new_emp_1 = Employee.from_string(emp_str_1)
#
# print(new_emp_1.__dict__)

import datetime

my_date = datetime.date(2023, 12, 18)

print(Employee.is_workday(my_date))
