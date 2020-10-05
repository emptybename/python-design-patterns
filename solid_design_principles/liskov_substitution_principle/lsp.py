from abc import ABC, abstractmethod


class Employee(ABC):

    @abstractmethod
    def bonus(self): pass


class PermanentEmployee(Employee):
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def bonus(self):
        return self.salary * .6


class TemperoryEmployee(Employee):
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def bonus(self):
        return self.salary * .5


# Till now we are following the LSP
# But if we add another type of employee which does not have bonus method then it will break LSP

# e.g

# Break LSP
class ContractEmployee(Employee):
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def bonus(self):
        raise Exception
