"""
In builder Facets if new info comes other than address and job then we will loose open close principal.
So to avoid that we will use inheritance
"""


class Person:
    def __init__(self):
        self.name = None
        self.position = None
        self.dob = None

    def __str__(self):
        return f'Name: {self.name}, works as {self.position}, Date of birth: {self.dob}'

    @staticmethod
    def new():
        return PersonBuilder()


class PersonBuilder:
    def __init__(self):
        self.person = Person()

    def build(self):
        return self.person


class PersonNameBuilder(PersonBuilder):
    def called(self, name):
        self.person.name = name
        return self


class PersonJobBuilder(PersonNameBuilder):
    def works_as(self, position):
        self.person.position = position
        return self


class PersonDobBuilder(PersonJobBuilder):
    def date_of_birth(self, dob):
        self.person.dob = dob
        return self


if __name__ == "__main__":
    pd = PersonDobBuilder()
    person = pd.called("mayank").works_as("SSE").date_of_birth("1/2/2000").build()
    print(person)
