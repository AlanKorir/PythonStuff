class Person:
    def __init__(self, firstName, lastName, salary):
        # self.age = age
        # self.weight = weight
        # self.height = height
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary
        # self.catch = catch

    def fullname(self):
        return '{} {}'.format(self.firstName, self.lastName)

    def employeeRaise(self):
        self.salary = int(self.salary * 1.4)

user1 =  Person("John", "Doe", 300000)
user1.employeeRaise()
print(user1.salary)


