"""
Decorator pattern facilitates the addition of behaviour without altering the class itself or inheriting from it.
Structural design pattern.
Used to dynamically (at runtime) add functionality to some object.
Flexible alternative to subclassing for extending functionality (composition over inheritance).
Decorators are wrapped around a particular component.
Decorators can wrap themselves.

Implementation:
- abstract base class
- abstract decorator_pattern for that class
- decorator_pattern hierarchy instead of subclass hierarchy

Each kind of additional functionality is included within a separate class - single responsibility principle.
it is possible to include several additional functionalities by sequentially using decorators.

Decouple different behaviors so that you compose them in any way you like.

Motivation:
- want to augment an object with additional functionality
- do not want to rewrite or alter existing code (open-closed principle)
- want to keep new functionality separate (single responsibility principle)
- need to be able to interact with existing structures
Two options to achieve this:
a) inherit from an object of interest (if possible)
b) build a decorator which references the decorated object adding new features on top of it
"""

from abc import ABC, abstractmethod


class Creature(ABC):

    @abstractmethod
    def feed(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def make_noise(self):
        pass


class Animal(Creature):

    def feed(self):
        print("I eat grass")

    def move(self):
        print("I walk forward")

    def make_noise(self):
        print("WOOO!")


class AbstractDecorator(Creature):

    def __init__(self, base):
        self.base = base

    def feed(self):
        self.base.feed()

    def move(self):
        self.base.move()

    def make_noise(self):
        self.base.make_noise()


class Swimming(AbstractDecorator):

    def move(self):
        print("I swim forward")

    def make_noise(self):
        print("...")


class Predator(AbstractDecorator):

    def feed(self):
        print("I eat other animals")


class Fast(AbstractDecorator):

    def move(self):
        self.base.move()
        print("Fast!")


animal = Animal()
swimming = Swimming(animal)
predator = Predator(swimming)
fast = Fast(predator)
faster = Fast(fast)

faster.base.base = faster.base.base.base

