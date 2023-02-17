"""
Prototype - a partially or fully initialized object that you copy (clone) and make use of.
When it's easier to copy an existing object to fully initialize a new one.
Intent - to solve the problem of duplication.

Motivation:
- complicated objects (e.g. cars) aren't designed from scratch - they reiterate existing designs
- an existing (partially or fully constructed) design is a Prototype
- we make a copy (clone) of the prototype and customize it (requires "deep copy" support)
- we make the cloning convenient (e.g. via a Factory)

Implementation:
- partially construct an object and store it somewhere
- deep copy the prototype
- customize the resulting instance
- a factory provides a convenient API for using prototypes


Example - prototype is used when creating a named tuple with default parameters:

Vector2D = namedtuple("Vector2D", "x1 y1 x2 y2 origin_x origin_y")
vector_zero = Vector2D(0, 0, 0, 0, 0, 0)  # vector_zero is a prototype
v1 = vector_zero._replace(x1=10, y1=10, x2=20, y2=20)  # we're not using Vector2D class anymore for creating instances
(we're using an existing instance of Vector2D class)
"""

import copy


class Address:
    def __init__(self, street_address, city, country):
        self.street_address = street_address
        self.city = city
        self.country = country

    def __str__(self):
        return f"{self.street_address}, {self.city}, {self.country}"


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f"{self.name} lives at {self.address}"


john = Person("John", Address("123 London Road", "London", "UK"))
print(john)

jane = john  # let's suppose we want to add Jane living at the same address
jane.name = "Jane"  # this won't work - both "john" and "jane" refer to the same object

# one more attempt
address = Address("123 London Road", "London", "UK")
john = Person("John", address)
jane = Person("Jane", address)
jane.address.street_address = "123B London Road"  # this won't work - both John and Jane keep reference to the same address object
print(jane)
print(john)

# how to solve - deep copy - performs recursive copying of all the attributes of an object, thereby making a new object
# that doesn't refer to the original
john = Person("John", Address("123 London Road", "London", "UK"))
jane = copy.deepcopy(john)  # allows us to reuse address object from above
jane.name = "Jane"
jane.address.street_address = "124 London Road"
print(john)
print(jane)
