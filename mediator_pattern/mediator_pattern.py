"""
Mediator is a component that facilitates communication between other components without them necessarily being aware of
each other or having direct (reference) access to each other.

Mediator engages in bidirectional communication with its connected components:
- mediator has functions that components can call;
- components have functions the mediator can call.

Motivation:
- components may go in and out of a system at any time (chat root members, MMORPG players, etc.)
- it makes no sense for them to have direct references to one another (those references may go dead, etc.)
- Solution: to have all components refer to some central component that facilitates communication (all communication
is handled by mediator).

GoF: allows loose coupling by encapsulating the way disparate sets of objects interact and communicate with each other.
Allows for the actions of each object set to vary independently of one another.
"""


class Person:
    def __init__(self, name):
        self.name = name
        self.chat_log = []
        self.room = None

    def receive(self, sender, message):
        formatted_message = f"{sender}: {message}"
        print(f"[{self.name}'s chat session] {formatted_message}")
        self.chat_log.append(formatted_message)

    def private_message(self, who_to, message):
        self.room.message(self.name, who_to, message)

    def say(self, message):
        self.room.broadcast(self.name, message)


class ChatRoom:  # central mediator
    def __init__(self):
        self.people = []

    def join(self, person):
        join_msg = f"{person.name} joins the chat"
        self.broadcast("room", join_msg)
        person.room = self
        self.people.append(person)

    def broadcast(self, source, message):
        for person in self.people:
            if person.name != source:
                person.receive(source, message)

    def message(self, source, destination, message):
        for person in self.people:
            if person.name == destination:
                person.receive(source, message)


if __name__ == "__main__":
    room = ChatRoom()

    john = Person("John")
    jane = Person("Jane")

    room.join(john)
    room.join(jane)

    john.say("Hi room!")
    jane.say("Oh, hey John!")

    simon = Person("Simon")
    room.join(simon)
    simon.say("Hi everyone!")

    jane.private_message("Simon", "Glad you could join us!")
