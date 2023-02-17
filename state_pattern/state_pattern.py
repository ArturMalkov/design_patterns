"""
State pattern is a pattern in which object's behavior is determined by its state.
A way of managing state machine in OOP fashion - an object will behave differently depending on what state it's in
(no matter how it got into that state).
State1 -> state2 -> state3, etc.

"state" is an instance variable telling whether an object is now "open" or "closed" - it contains a state object (
which will implement different methods)

A formalized construct which manages state and transitions is called a state machine.

Allows an object to alter its behaviour when its internal state changes. The object will appear to change its class.

Changes in state can be explicit or in response to event (Observer pattern).

Formally define possible states and events/triggers.

You can define:
- state entry/exit behaviors
- action when a particular event causes a transition
- guard conditions enabling/disabling a transition
- default action when no transitions are found for an event
"""

from abc import ABC


class Switch:
    def __init__(self):
        self.state = OffState()  # maintains an instance of a concrete state subclass that defines the current state

    def on(self):
        self.state.on(self)

    def off(self):
        self.state.off(self)


class State(ABC):  # defines an interface for encapsulating the behavior associated with a particular state of the object
    def on(self, switch):
        print("Light is already on")

    def off(self, switch):
        print("Light is already off")


class OnState(State):  # implements a behavior associated with the state of the object
    def __init__(self):
        print("Light turned on")

    def off(self, switch):
        print("Turning light off...")
        switch.state = OffState()


class OffState(State):
    def __init__(self):
        print("Light turned off")

    def on(self, switch):
        print("Turning light on...")
        switch.state = OnState()


if __name__ == "__main__":
    switch = Switch()
    switch.off()
    switch.on()
    switch.on()
