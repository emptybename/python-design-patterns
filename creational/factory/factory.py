"""
Factory is basically creating a separate class with factory methods which return objects
"""
from math import sin, cos


class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return "x: {}, y: {}".format(self.x, self.y)


class PointFactory:

    def __int__(self) -> None:
        pass

    @staticmethod
    def new_cartesian_point(x: float, y: float) -> Point:
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho: float, theta: float) -> Point:
        return Point(rho * cos(theta), rho * sin(theta))


if __name__ == "__main__":
    p = PointFactory.new_cartesian_point(3, 4)
    p1 = PointFactory.new_polar_point(10, 30)
    print(p)
    print(p1)
