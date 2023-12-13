# Example Class
class Employee:
    #class variable
    raise_amount = 1.04
    num_of_emps= 0

    # init method -> constructor
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = str.lower(first) + '.' + str.lower(last) + '@company.com'

        Employee.num_of_emps += 1

    # class method
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


# Instance -> With init
emp_1 = Employee('Phyton', 'OOP', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(Employee.num_of_emps)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

emp_1.raise_amount = 1.05
Employee.raise_amount = 1.06

#Instance Variables
print(emp_1.raise_amount)


#Class Variables
print(Employee.raise_amount)