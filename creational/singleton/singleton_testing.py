"""
One of the drawback in Single pattern is that if you take direct dependency on it then you will get stuck.
To resolve this we should make it configurable
"""
import unittest


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=Singleton):
    def __init__(self):
        # Assume we have db of population for cities in a file name capitals.txt
        self.population = {}
        file = open('capitals.txt', 'r')
        lines = file.readlines()
        for i in range(0, len(lines), 2):
            city = lines[i].strip()
            self.population[city] = int(lines[i + 1].strip())
        file.close()


class SingletonRecordFinder:
    @staticmethod
    def total_population(cities):
        result = 0
        for city in cities:
            result += Database().population.get(city, 0)
        return result


class DummyDatabase(metaclass=Singleton):
    def __init__(self):
        self.population = {
            'alpha': 10,
            'beta': 20,
            'gamma': 30
        }


class ConfigurableRecordFinder:
    def __init__(self, db):
        self.db = db

    def total_population(self, cities):
        db = self.db
        result = 0
        for city in cities:
            result += db.population.get(city, 0)
        return result


class SingletonTest(unittest.TestCase):
    def test_is_singleton(self):
        db1 = Database()
        db2 = Database()
        self.assertEqual(db1, db2)

    def test_singleton_total_population(self):
        cities = ['Gwalior', 'Bhind']
        self.assertEqual(30, SingletonRecordFinder.total_population(cities))

    def test_dependent_total_population(self):
        ddb = DummyDatabase()
        cities = ['alpha', 'beta']
        crf = ConfigurableRecordFinder(ddb)
        self.assertEqual(30, crf.total_population(cities))


if __name__ == "__main__":
    unittest.main()
