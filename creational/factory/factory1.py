"""
Another example of factory. Give insurance to employed and un-employed persons
"""

from abc import ABC, abstractmethod


class Person(ABC):
    @abstractmethod
    def calculate_risk(self):
        pass


class Worker(Person):
    def __init__(self, name: str, age: int, hours: float) -> None:
        self.name = name
        self.age = age
        self.hours = hours

    def calculate_risk(self) -> float:
        return self.age + 100 / self.hours

    def __str__(self) -> str:
        return self.name + " [" + str(self.age) + "] - " + str(self.hours) + "h/week"


class UnEmployed(Person):
    def __init__(self, name: str, age: int, able: bool) -> None:
        self.name = name
        self.age = age
        self.able = able

    def calculate_risk(self) -> int:
        if self.able:
            return self.age + 10
        else:
            return self.age + 30

    def __str__(self) -> str:
        if self.able:
            return self.name + " [" + str(self.age) + "] - able to work"
        else:
            return self.name + " [" + str(self.age) + "] - unable to work"


class PersonFactory:

    @staticmethod
    def get_person(type_of_person):
        if type_of_person == "worker":
            return Worker("mayank", 27, 50)
        elif type_of_person == "unemployed":
            return UnEmployed("abc", 25, True)


if __name__ == "__main__":
    print(PersonFactory.get_person("worker"))
    print(PersonFactory.get_person("unemployed"))
