"""
A class should be open for extension but should be closed for modification. Do not touch already implemented interface!
Below we don't touch the base classes - we extend their functionality through inheritance or composition.
Bob Martin - original class and the new (extended) one should implement the same interface (as opposed to Bertrand Meyer's
view) so that client code won't need to change.

Do not touch existing code - as it is already tested and works properly.

Extensibility ensures small classes (instead of growing classes) and can help prevent code duplication (DRY).
"""
from abc import ABC, abstractmethod
from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name: str, color: Color, size: Size):
        self.name = name
        self.color = color
        self.size = size

    def __str__(self):
        return self.name


class ProductFilter:  # don't do this
    @staticmethod
    def filter_by_color(products, color):
        for product in products:
            if product.color == color:
                yield product

    @staticmethod
    def filter_by_size(products, size):
        for product in products:
            if product.size == size:
                yield product

    @staticmethod
    def filter_by_size_and_color(products, size, color):
        for product in products:
            if product.size == size and product.color == color:
                yield product

    # etc.
    # Adding other filter will explode the number of possible filter combinations.


# Enterprise pattern: Specification
class Specification(ABC):  # base class is closed for further modification once its API is finished; new features are to be added via subclasses (i.e. through extension)
    @abstractmethod
    def is_satisfied(self, item):
        pass

    def __and__(self, other):
        return AndSpecification(self, other)  # gives the ability to use 'and' keyword


class Filter(ABC):
    @abstractmethod
    def filter(self, items, spec):
        pass


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class AndSpecification(Specification):
    def __init__(self, spec1, spec2):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied(self, item):
        return self.spec1.is_satisfied(item) and \
               self.spec2.is_satisfied(item)


class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


apple = Product("Apple", Color.GREEN, Size.SMALL)
tree = Product("Tree", Color.GREEN, Size.LARGE)
house = Product("House", Color.BLUE, Size.LARGE)

products = [apple, tree, house]

bf = BetterFilter()

green = ColorSpecification(Color.GREEN)
print("Green products:")
for p in bf.filter(products, green):
    print(p)

large = SizeSpecification(Size.LARGE)
print("Large products:")
for p in bf.filter(products, large):
    print(p)

blue = ColorSpecification(Color.BLUE)
# large_blue = AndSpecification(large, blue)
large_blue = large and blue

print("Large blue products:")
for p in bf.filter(products, large_blue):
    print(p)
