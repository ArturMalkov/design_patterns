from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def __str__(self):
        return ""


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def resize(self, factor):
        self.radius *= factor

    def __str__(self):
        return f"A circle of radius {self.radius}"


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return f"A square with side {self.side}"


class ColoredShape(Shape):  # decorator
    def __init__(self, shape, color):
        if isinstance(shape, ColoredShape):
            raise Exception("Same decorator cannot be applied twice!")
        self.shape = shape
        self.color = color

    def __str__(self):
        return f"{self.shape} has the color {self.color}"


class TransparentShape(Shape):  # decorator
    def __init__(self, shape, transparency):
        if isinstance(shape, TransparentShape):
            raise Exception("Same decorator cannot be applied twice!")
        self.shape = shape
        self.transparency = transparency

    def __str__(self):
        return f"{self.shape} has {self.transparency*100}% transparency"


if __name__ == "__main__":
    circle = Circle(2)
    print(circle)

    red_circle = ColoredShape(circle, "red")
    print(red_circle)

    red_half_transparent_circle = TransparentShape(red_circle, 0.5)
    print(red_half_transparent_circle)

    # mixed = ColoredShape(ColoredShape(Square(4), "red"), "green")
    # print(mixed)
    # green_red_circle = ColoredShape(red_circle, "green")
    # print(green_red_circle)
