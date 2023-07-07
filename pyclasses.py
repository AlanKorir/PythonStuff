class Employee:
    raiseAmount = 1.4
    def __init__(self, firstName, lastName, employeeSalary):
        self.firstName = firstName
        self.lastName = lastName
        self.employeeSalary = employeeSalary

    def fullName(self):
        return '{} {}'.format(self.firstName, self.lastName)

    def giveRaise(self):
        self.employeeSalary = int(self.employeeSalary * self.raiseAmount)

    def employeeEmail(self):
        return self.firstName + '@organization.com'


employee1 = Employee('John', 'Doe', 30000)

class Developer(Employee):
    pass

dev1 = Developer('James', 'Atkinson', 90000)
print(dev1.__dict__)




