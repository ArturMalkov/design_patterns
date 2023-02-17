from abc import ABC, abstractmethod


class ObservableEngine:
    def __init__(self):
        self.__subscribers = set()

    def subscribe(self, subscriber):
        self.__subscribers.add(subscriber)

    def unsubscribe(self, subscriber):
        if subscriber in self.__subscribers:
            self.__subscribers.remove(subscriber)

    def notify(self, achievement):
        for subscriber in self.__subscribers:
            subscriber.update(achievement)


class AbstractObserver(ABC):
    @abstractmethod
    def update(self, achievement):
        pass


class ShortNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = set()

    def update(self, achievement):
        self.achievements.add(achievement["title"])


class FullNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = []

    def update(self, achievement):
        if achievement not in self.achievements:
            self.achievements.append(achievement)


# aurora_engine = ObservableEngine()
# short_notifier = ShortNotificationPrinter()
# full_notifier = FullNotificationPrinter()
#
# aurora_engine.subscribe(short_notifier)
# aurora_engine.subscribe(full_notifier)
# # print(aurora_engine._ObservableEngine__subscribers)
# aurora_engine.notify({"title": "Покоритель", "text": "Дается при выполнении всех заданий в игре"})
#
# print(short_notifier._ShortNotificationPrinter__achievements)
