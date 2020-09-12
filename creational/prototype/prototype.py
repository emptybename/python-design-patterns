from copy import deepcopy


class Address:
    def __init__(self, street_address, city, country):
        self.street_address = street_address
        self.city = city
        self.country = country


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'Name: {self.name} ' + \
               f'Address: {self.address.street_address}, {self.address.city}, {self.address.country}'


if __name__ == '__main__':
    john = Person('john', Address('123 London Road', 'London', 'UK'))
    jane = deepcopy(john)
    jane.name = 'jane'
    jane.address.street_address = '124 London Road'
    print(john, '\n', jane)
