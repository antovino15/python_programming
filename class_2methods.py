class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp1 = Employee('vino', 'anto', 60000)
emp2 = Employee('Shan', 'vino', 70000)
print(emp2.email)
print(emp1.fullname())
