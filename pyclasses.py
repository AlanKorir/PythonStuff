class Person:
    def __init__(self, firstName, lastName):
        # self.age = age
        # self.weight = weight
        # self.height = height
        self.firstName = firstName
        self.lastName = lastName
        # self.catch = catch

    def fullname(self):
        return '{} {}'.format(self.firstName, self.lastName)


user1 =  Person("John", "Doe")
print(user1.fullname())


