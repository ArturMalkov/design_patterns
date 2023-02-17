"""
Observer pattern is one of the most common design patterns.
Behavioral design pattern that defines a one-to-many dependency between objects so that when one object changes state,
all its dependents are notified and updated automatically.
2 objects - observer and observable.
An observer is an object that wishes to be informed about events happening in the system.
The entity generating the events is an observable.
Needed for notifying observer object about changes in observable object.
Push system - observable object notifies the observer itself, not vice-versa (instead of pull)

Motivation:
- we need to be informed when certain things happen (object's property changes, etc.)
- we want to listen to events and be notified when they occur (notifications should include useful data - who generated the
event, which values were generated)
- we want to unsubscribe from events if we're no longer interested
"""

from abc import ABC, abstractmethod


class NotificationManager:
    def __init__(self):
        self.__subscribers = set()

    def subscribe(self, subscriber):
        self.__subscribers.add(subscriber)

    def unsubscribe(self, subscriber):
        self.__subscribers.remove(subscriber)

    def notify(self, message):
        for subscriber in self.__subscribers:
            subscriber.update(message)


class AbstractObserver(ABC):
    def __init__(self, name):
        self._name = name

    @abstractmethod
    def update(self, message):
        pass


class MessageNotifier(AbstractObserver):
    def update(self, message):
        print(f"{self._name} received message!")


class MessagePrinter(AbstractObserver):
    def update(self, message):
        print(f"{self._name} received message: {message}")


notifier = MessageNotifier("Notifier1")
printer1 = MessagePrinter("Printer1")
printer2 = MessagePrinter("Printer2")

manager = NotificationManager()
manager.subscribe(notifier)
manager.subscribe(printer1)
manager.subscribe(printer2)
manager.notify("Hello!")
