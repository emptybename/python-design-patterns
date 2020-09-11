"""
Creating Factories for different objects
"""

from abc import ABC, abstractmethod
from enum import Enum, auto


class HotDrink(ABC):
    @abstractmethod
    def consume(self):
        pass


class Tea(HotDrink):
    def consume(self):
        print("This Tea is delicious")


class Coffee(HotDrink):
    def consume(self):
        print("This Coffee is delicious")


class HotDrinkFactory(ABC):
    def prepare(self, amount):
        pass


class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print("Put Tea bag, boil water")
        print("Pour {}ml and enjoy!".format(amount))
        return Tea()


class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print("Put Beans, grind them")
        print("Pour {}ml and enjoy!".format(amount))
        return Coffee()


class HotDrinkMachine:
    class AvailableDrink(Enum):
        TEA = auto()
        COFFEE = auto()

    factories = []
    initialized = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            for d in self.AvailableDrink:
                name = d.name.capitalize()
                factory_instance = eval(name + "Factory")()
                self.factories.append((name, factory_instance))

    def make_drink(self):
        print("Available Drinks!")
        for drink in self.factories:
            print(drink[0])
        print("Select drink from 0 - {}".format(len(self.factories) - 1))
        drink = input('')
        idx = int(drink)
        print("select amount of drink")
        amount = int(input(''))
        return self.factories[idx][1].prepare(amount)


if __name__ == "__main__":
    hdm = HotDrinkMachine()
    drink = hdm.make_drink()
    drink.consume()
