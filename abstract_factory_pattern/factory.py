"""
Factory - an entity (e.g. class) that can take care of object creation
Factory can be external or reside inside the object as a nested class


Example - 'namedtuple' function from 'collections' module is a class factory - it returns a class:

Vector2D = namedtuple("Vector2D", "x1 y1 x2 y2 origin_x origin_y")  # Vector2D is a class
vector_zero = Vector2D(10, 10, 20, 20, 0, 0)  # vector_zero is an instance
"""

from enum import Enum
from math import *


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"

    class PointFactory:
        def new_cartesian_point(self, x, y):  # may be static as well
            return Point(x, y)

        def new_polar_point(self, rho, theta):  # may be static as well
            return Point(rho * cos(theta), rho * sin(theta))


if __name__ == "__main__":
    p = Point(2, 3)
    p2 = Point.PointFactory.new_polar_point(1, 2)
    print(p, p2, sep="\n")
