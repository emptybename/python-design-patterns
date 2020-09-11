"""
create a main course and a dessert at an Italian and a French restaurant, but you won't mix one cuisine with the other.
"""

from abc import ABC, abstractmethod
from enum import Enum, auto


class Dish(ABC):
    @abstractmethod
    def cook(self):
        pass


class ItalianMainCourse(Dish):

    def cook(self):
        print("ItalianMainCourse is prepared")


class ItalianDessertCourse(Dish):

    def cook(self):
        print("Italian dessert is prepared")


class FrenchMainCourse(Dish):
    def cook(self):
        print("French Main course is prepared")


class FrenchDessertCourse(Dish):
    def cook(self):
        print("French Dessert is prepared")


class RestaurantFactory(ABC):
    @abstractmethod
    def get_dish(self, dish_type):
        pass


class ItalianRestaurantFactory(RestaurantFactory):
    class AvailableDish(Enum):
        MAIN = auto()
        DESSERT = auto()

    initialize = False

    def __init__(self):
        if not self.initialize:
            self.initialize = True
            self.italian_dishes = {}
            for d in self.AvailableDish:
                self.italian_dishes[d.name] = eval("Italian" + d.name.capitalize() + "Course")()

    def get_dish(self, dish_type):
        return self.italian_dishes[dish_type.upper()]


class FrenchRestaurantFactory(RestaurantFactory):
    class AvailableDish(Enum):
        MAIN = auto()
        DESSERT = auto()

    initialize = False

    def __init__(self):
        if not self.initialize:
            self.initialize = True
            self.french_dishes = {}
            for d in self.AvailableDish:
                self.french_dishes[d.name] = eval("French" + d.name.capitalize() + "Course")()

    def get_dish(self, dish_type):
        return self.french_dishes[dish_type.upper()]


class Restaurant:
    class AvailableRestaurant(Enum):
        ITALIAN = auto()
        FRENCH = auto()

    initialize = False
    restaurants_factories = []

    def __init__(self):
        if not self.initialize:
            self.initialize = True
            for d in self.AvailableRestaurant:
                name = d.name.capitalize()
                factory_instance = eval(name + "RestaurantFactory")()
                self.restaurants_factories.append((name, factory_instance))

    def get_dish(self):
        print("Available Restaurants")
        for idx in range(0, len(self.restaurants_factories)):
            print(idx, self.restaurants_factories[idx][0])
        print("Please select restaurant number from 0 - {}".format(len(self.restaurants_factories) - 1))

        restaurant = input('')
        idx = int(restaurant)
        print("Please select dish type 'main' or 'dessert' ")
        dish_type = input('')
        return self.restaurants_factories[idx][1].get_dish(dish_type)


if __name__ == "__main__":
    res = Restaurant()
    dish = res.get_dish()
    dish.cook()

