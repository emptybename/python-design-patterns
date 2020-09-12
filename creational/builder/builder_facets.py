"""
Create Person object using multiple builders
"""


class Person:
    def __init__(self):
        # Address
        self.street_address = None
        self.city = None
        self.postcode = None
        # Company
        self.company = None
        self.position = None
        self.annual_income = None

    def __str__(self):
        return f'Address: {self.street_address}, {self.postcode}, {self.city}' + \
               f'Employed at: {self.company} as a {self.position} earning{self.annual_income}'

    @staticmethod
    def initialize():
        return PersonBuilder()


class PersonBuilder:
    def __init__(self, person=Person()):
        self.person = person

    @property
    def works(self):
        return PersonJobBuilder(self.person)

    @property
    def lives(self):
        return PersonAddressBuilder(self.person)

    def __str__(self):
        return str(self.person)


class PersonJobBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def at(self, company):
        self.person.company = company
        return self

    def position(self, position):
        self.person.position = position
        return self

    def earning(self, income):
        self.person.annual_income = income
        return self


class PersonAddressBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def at(self, street_address):
        self.person.street_address = street_address
        return self

    def postcode(self, postcode):
        self.person.postcode = postcode
        return self

    def in_city(self, city):
        self.person.city = city
        return self


if __name__ == "__main__":
    # person = Person.initialize() or
    builder = PersonBuilder()
    builder = builder.works\
        .at('pikachu')\
        .position('SSE')\
        .earning(1200000)\
        .lives.at('REpublic')\
        .postcode('560037')\
        .in_city('Bangalore')
    print(builder)
