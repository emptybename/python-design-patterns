"""
In monostate design pattern, resources are shared by every objects
"""


class CEO:
    __shared_state = {
        "name": "Steve",
        "age": 40
    }

    def __init__(self):
        self.__dict__ = self.__shared_state

    def __str__(self):
        return f'{self.name} is {self.age} years old'


class Monostate:
    __shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__shared_state
        return obj


class CFO(Monostate):
    def __int__(self):
        self.name = ''
        self.money_manage = 0

    def __str__(self):
        return f'{self.name} manage ${self.money_manage} money'


if __name__ == "__main__":
    ceo1 = CEO()
    print(ceo1)
    ceo2 = CEO()
    ceo2.age = 60
    print(ceo1)
    print(ceo2)

    cfo = CFO()
    cfo.name = "mayank"
    cfo.money_manage = 10
    print(cfo)

    cfo1 = CFO()
    print(cfo1.__dict__)
