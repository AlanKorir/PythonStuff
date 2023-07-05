class Person:
    numOfPersons = 0

    raiseAmount = 1.04 

    def __init__(self, firstName, lastName, salary):
        # self.age = age
        # self.weight = weight
        # self.height = height
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary
        # self.catch = catch
        
        Person.numOfPersons += 1

    def fullname(self):
        return '{} {}'.format(self.firstName, self.lastName)

    def employeeRaise(self):
        self.salary = int(self.salary * self.raiseAmount)

user1 =  Person("John", "Doe", 300000)
user2 = Person("Jane", "Doe", 40000)
Person.raiseAmount = 2.06
user1.employeeRaise()

print(user1.salary)
print(Person.raiseAmount)
print (Person.numOfPersons)

