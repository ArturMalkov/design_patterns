"""
Template method defines the sceleton of an algorithm deferring some steps to subclasses. Template method lets subclasses redefine (override)
certain steps of an algorithm without changing the algorithm structure.
It is a high-level blueprint for an algorithm to be completed by inheritors.
As opposed to strategy pattern (which relies on composition), template method decomposes algorithms into common parts + specifics
via inheritance.
It helps you reuse certain structure across multiple cases, with the possibility of changing what varies from case
to case.

AbstractClass -> ConcreteClass

Template method is a high-level algorithm defined in abstract/parent class. Some pieces of its concrete implementation
that you don't know/can't foresee how they will look like/how they should perform in a particular scenario/concretion of
that template/use case of that template, should be deferred to subclasses. Therefore, they should be abstract. Subclasses should implement them.
Subclasses supply the implementation of particular operations that are missing in the template method.

When some options of your algorithm vary across specific instances, while others do not (consistent, or invariant).

- define an algorithm at a high level in parent class
- define constituent parts as abstract methods
- inherit the algorithm class providing necessary overrides
"""

from abc import ABC, abstractmethod


class Game(ABC):
    def __init__(self, number_of_players):
        self.number_of_players = number_of_players
        self.current_player = 0

    def run(self):  # this is a template method! it uses lots of members which are to be implemented by inheritors.
        self.start()
        while not self.have_winner():
            self.take_turn()
        print(f"Player {self.winning_player} wins!")

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def have_winner(self):
        pass

    @abstractmethod
    def take_turn(self):
        pass

    @abstractmethod
    @property
    def winning_player(self):
        pass


class Chess(Game):
    def __init__(self):
        super().__init__(2)  # chess is always a game of two - no parameters needed
        self.max_turns = 10
        self.turn = 1

    def start(self):
        print(f"Starting a game of chess with {self.number_of_players} players.")

    def have_winner(self):
        return self.turn == self.max_turns

    def take_turn(self):
        print(f"Turn {self.turn} taken by player {self.current_player}")
        self.turn += 1
        self.current_player = 1 - self.current_player

    @property
    def winning_player(self):
        return self.current_player


if __name__ == "__main__":
    chess = Chess()
    chess.run()
