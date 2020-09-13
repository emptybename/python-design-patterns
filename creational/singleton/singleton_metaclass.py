"""
Foo(*args, **kwargs) is equivalent to Foo.__call__(*args, **kwargs).
Since Foo is an instance of type, Foo.__call__(*args, **kwargs) calls type.__call__(Foo, *args, **kwargs).
type.__call__(Foo, *args, **kwargs) calls type.__new__(Foo, *args, **kwargs) which returns obj.
obj is then initialized by calling obj.__init__(*args, **kwargs).
obj is returned.

"""


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        # print(cls.__dict__)
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
            # print(cls._instances[cls])
        return cls._instances[cls]


class Database(metaclass=Singleton):
    def __init__(self):
        print("Loading Database")


if __name__ == "__main__":
    d1 = Database()
    d2 = Database()
    print(d1 is d2)
