"""
Using factory method we can meaningfully create an object otherwise we have to use if statement for
different point creation
"""
from enum import Enum
from math import sin, cos


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class Point:
    """
    As we can see as the number of coordinate system increases conditional statement increases which is not scalable
    """

    # def __init__(self, a, b, system=CoordinateSystem.CARTESIAN):
    #     if system == CoordinateSystem.CARTESIAN:
    #         self.x = a
    #         self.y = b
    #     elif system == CoordinateSystem.POLAR:
    #         self.x = a*cos(b)
    #         self.y = a*sin(b)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "x : {}, y: {}".format(self.x, self.y)

    """
    Creating factory method to create object
    """

    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * cos(theta), rho * sin(theta))


if __name__ == "__main__":
    p = Point.new_cartesian_point(4, 5)
    p1 = Point.new_polar_point(10, 30)
    print(p)
    print(p1)
