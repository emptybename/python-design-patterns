"""
In this example, you will see that you get the same object reference but initializer is called two times which
you don't want. So this is a half way process of singleton pattern
"""

import random


class Database:
    _instance = None

    def __init__(self):
        print("id = ", random.randint(1, 100))

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)
        return cls._instance


if __name__ == "__main__":
    d1 = Database()
    d2 = Database()
    print(d1 == d2)
