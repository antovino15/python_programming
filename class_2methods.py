class Employee:
    raise_amount = 2.0
    emp_count = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.emp_count += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def pay_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount


emp1 = Employee('vino', 'anto', 60000)
emp2 = Employee('Shan', 'vino', 70000)

Employee.set_raise_amt(3)
print(Employee.raise_amount)
print(emp1.pay)
emp1.pay_raise()
print(emp1.pay)
# print(emp2.email)
# print(emp1.fullname())

# Regular methjos to a class mehod by adding decorator.
