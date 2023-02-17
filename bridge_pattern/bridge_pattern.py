"""
Bridge pattern is about connecting components together through abstractions.
Bridge pattern is a mechanism that decouples an interface (hierarchy) from an implementation (hierarchy).
The intent of the bridge pattern is to decouple abstraction from implementation

Bridge pattern connects 2 hierarchies of different classes.

Motivation:
- Bridge prevents a "Cartesian product" complexity explosion of the number of entities (classes) as you get more
combinations of different classes.
"""

# circle or square
# vector or raster

# VectorCircle, VectorSquare, RasterCircle, RasterSquare - this approach doesn't scale

from abc import ABC, abstractmethod


class Renderer(ABC):
    @abstractmethod
    def render_circle(self, radius):
        pass

    # render_square()


class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print(f"Drawing circle of radius {radius}")


class RasterRenderer(Renderer):
    def render_circle(self, radius):
        print(f"Drawing pixels for a circle of radius {radius}")


class Shape(ABC):
    def __init__(self, renderer):  # core of the Bridge pattern! - connects 2 hierarchies of classes
        self.renderer = renderer

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def resize(self, factor):
        pass


class Circle(Shape):
    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        self.renderer.render_circle(self.radius)

    def resize(self, factor):
        self.radius *= factor


if __name__ == "__main__":
    raster = RasterRenderer()
    vector = VectorRenderer()
    circle = Circle(vector, 5)
    circle.draw()
    circle.resize(2)
    circle.draw()
