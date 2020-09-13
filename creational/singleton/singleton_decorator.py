"""
In Single allocator __init__ was calling multiple times as we were creating instances using __new__ because __init__
calls just after __new__ that we want to stop.
"""


def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
            # print(instances[class_])
        return instances[class_]

    return get_instance


@singleton
class Database:
    def __init__(self):
        print("Database loading")


if __name__ == "__main__":
    d1 = Database()
    d2 = Database()
    print(d1, d2)
