"""
If you have an interface that takes some sort of base class, you should be able to stick in any derived class in there
and it should work correctly.
I.e. you should be able to substitute a base type for a subtype (i.e. parent class with a child class).
(objects should be replaceable with instances of their subclasses without altering the behavior)

In other words, subclass should extend but not replace (contradict) the behavior/functionality of the base class.

If smth is true about the parent class, it has to be true about its child classes as well.
This principle forces you to model your inheritance hierarchies correctly - especially re choosing and modelling base classes.

One more wording: subclass shouldn't require of the code that calls it more than its parent does, and shouldn't return to
it less that its parent does.
"""


class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def area(self):
        return self._width * self._height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    def __str__(self):
        return f"Width: {self._width}, height: {self._height}"


class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._height = self._width = value


def use_it(rc):  # function only works on a rectangle but doesn't work on any derived class
    w = rc.width
    rc.height = 10  # for squares this line of code should change width as well, but its value has already been stored above
    expected = int(w * 10)
    print(f"Expected an area of {expected}, got {rc.area}")

