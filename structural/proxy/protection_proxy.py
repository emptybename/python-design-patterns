class Driver:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class CarProxy:
    def __init__(self, driver):
        self._car = Car(driver)

    def drive(self):
        if self._car.driver.age >= 16:
            self._car.drive()
        else:
            print(f"{self._car.driver.name} is too young to drive")


class Car:
    def __init__(self, driver):
        self.driver = driver

    def drive(self):
        print(f"Car is driven by {self.driver.name}")


if __name__ == '__main__':
    driver = Driver('John', 18)
    driver1 = Driver('Jane', 12)
    car = CarProxy(driver)
    car.drive()
    car1 = CarProxy(driver1)
    car1.drive()
