class Person:
    'All persons'

    personCount = 0

    def __init__(self, name):
        Person.personCount += 1
        self.id = Person.personCount
        self.name = name
        self.totalAmount = 0

    def pays(self, amount):
        self.totalAmount -= amount

    def receives(self, amount):
        self.totalAmount += amount

    def showDetails(self):
        print(self.id)
        print(self.name)
        print(self.totalAmount)
