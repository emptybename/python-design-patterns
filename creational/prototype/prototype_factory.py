from copy import deepcopy


class Address:
    def __init__(self, street_address, city, suite):
        self.street_address = street_address
        self.city = city
        self.suite = suite

    def __str__(self):
        return f'{self.street_address}, Suite: #{self.suite}, City:{self.city}'


class Employee:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'{self.name} works at {self.address}'


class EmployeeFactory:
    main_office_employee = Employee('', Address('123A London Street', 'London', ''))
    aux_office_employee = Employee('', Address('123B London Street', 'London', ''))

    @staticmethod
    def __new_employee(proto, name, suite):
        employee = deepcopy(proto)
        employee.name = name
        employee.address.suite = suite
        return employee

    @staticmethod
    def new_main_office_employee(name, suite):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.main_office_employee,
            name, suite
        )

    @staticmethod
    def new_aux_office_employee(name, suite):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.aux_office_employee,
            name, suite
        )


if __name__ == "__main__":
    emp1 = EmployeeFactory.new_main_office_employee('mak', 30)
    emp2 = EmployeeFactory.new_aux_office_employee('pooja', 300)
    print(emp1)
    print(emp2)
