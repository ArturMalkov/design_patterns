"""
Factory - a component responsible solely for the wholesale (not piecewise) creation of objects.
Provides an interface for creating families of related or dependent objects (e.g. products of kind A and B
(which both make sense together!)) without specifying their concrete classes (that is the job of any particular concrete factory).
Unlike factory pattern, abstract factory constructs multiple objects.
Thus, abstract factory makes use of factory methods - one factory can comprise several factory methods.

Solution: create abstract class - Abstract Factory - which defines an interface for creating specific classes.

Motivation:
- object creation logic becomes too convoluted (we may not even know beforehand which object will be created - TBD at runtime dynamically);
- initializer is not descriptive:
        - name is always "__init__"
        - cannot overload with same sets of arguments with different names
        - can turn into "optional parameter hell"
- wholesale object creation (not piecewise, like in Builder) can be outsourced to:
a) a separate method (Factory Method)
b) a separate class (Factory)
c) a hierarchy of factories (Abstract Factory)


Pros of abstract factory:
- isolates specific classes: since abstract factory encapsulates the responsibility of creating classes and the creation
process itself, it isolates client from details of implementation of such classes;
- can easily (at runtime) be substituted with another abstract factory.

Cons of abstract factory:
- fixes the set of objects which can be created. Extending abstract factory for the purpose of creating new objects
can be difficult.
"""


from abc import ABC, abstractmethod


# class HeroFactory(ABC):
#     @abstractmethod
#     def create_hero(self, name):
#         pass
#
#     @abstractmethod
#     def create_spell(self):
#         pass
#
#     @abstractmethod
#     def create_weapon(self):
#         pass


class HeroFactory:
    @classmethod
    def create_hero(cls, name):
        return cls.Hero(name)

    @classmethod
    def create_spell(cls):
        return cls.Spell()

    @classmethod
    def create_weapon(cls):
        return cls.Weapon()


# class MagicFactory(HeroFactory):
#     def create_hero(self, name):
#         pass
#
#     def create_spell(self):
#         pass
#
#     def create_weapon(self):
#         pass


class WarriorFactory(HeroFactory):
    # def create_hero(self, name):
    #     return Warrior(name)
    #
    # def create_spell(self):
    #     return Power()
    #
    # def create_weapon(self):
    #     return Claymore()

    class Hero:
        def __init__(self, name):
            self.name = name
            self.spell = None
            self.weapon = None

        def add_weapon(self, weapon):
            self.weapon = weapon

        def add_spell(self, spell):
            self.spell = spell

        def hit(self):
            print(f"Warrior {self.name} hits the enemy with {self.weapon.hit()}")

        def cast(self):
            print(f"Warrior {self.name} casts the enemy with {self.spell.cast()}")

    class Weapon:
        @staticmethod
        def hit():
            return "Hit Claymore!"

    class Spell:
        @staticmethod
        def cast():
            return "Power"


def create_hero(factory):
    hero = factory.create_hero("Terminator")
    weapon = factory.create_weapon()
    spell = factory.create_spell()

    hero.add_weapon(weapon)
    hero.add_spell(spell)

    return hero


player = create_hero(WarriorFactory())
player.hit()
player.cast()
