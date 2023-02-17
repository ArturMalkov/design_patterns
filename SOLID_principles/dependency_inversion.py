"""
Don't confuse with dependency injection!

1. High-level classes/modules in your code shouldn't depend directly on low-level modules/concretions. Instead, they should depend on
abstractions (i.e. depend on interfaces rather than concrete implementations because this way you can swap one for the other)
2. Abstractions shouldn't depend on details. Details should depend on abstractions.

Couple to interfaces, not to classes / couple to abstractions, not to implementations (concretions), i.e. you should
depend on abstractions, not concretions.

Inversion - in the 'consuming' code we no longer care which exact type of object was passed to it, instead we invert the
dependency - we don't depend on the exact type of object passed - we force whoever is instantiating it to provide us an object
which fulfills certain contract (interface) (instead of us checking the type of the passed object internally, i.e. within the consuming code).

To avoid dependency on internal implementations of low-level modules.

Use ABC and abstract methods
"""
from abc import abstractmethod
from enum import Enum


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name


class RelationshipBrowser:  # abstraction/interface
    @abstractmethod
    def find_all_children_of(self, name):
        pass


class Relationships(RelationshipBrowser):  # low-level module
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.CHILD, parent)
        )

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name


class Research:  # high-level module
    # def __init__(self, relationships):
    #     relations = relationships.relations  # accessing internal storage mechanism of Relationships (a low-level module)
        # for r in relations:
        #     if r[0].name == "John" and r[1] == Relationship.PARENT:
        #         print(f"John has a child called {r[2].name}.")

    def __init__(self, browser):  # now it doesn't depend on any internal mechanics/the way relations are actually stored
        for p in browser.find_all_children_of("John"):
            print(f"John has a child called {p}")


parent = Person("John")
child1 = Person("Chris")
child2 = Person("Matt")

relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

Research(relationships)
