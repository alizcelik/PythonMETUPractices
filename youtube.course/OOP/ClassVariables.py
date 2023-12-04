# Example Class
class Employee:

    # init method -> constructor
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = str.lower(first) + '.' + str.lower(last) + '@company.com'

    # class method
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


# Instance -> Without init