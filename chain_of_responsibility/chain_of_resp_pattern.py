"""
Chain of responsibility - a chain of components who all get a chance to process a command or a query, optionally
having default processing implementation and an ability to terminate the processing chain.
Behavioral design pattern.
Represents a sequence of handlers processing an event one after another.
Passes the task/event to the next handler if the current one isn't able to handle it by itself.

Most commonly implemented as a chain of references (linked list):
- enlist objects in the chain, possibly controlling their order (method chain) or
- simply use a list (broker chain)

Every element of the chain can stop the processing of the element in addition to just passing it all along.
"""

QUEST_SPEAK, QUEST_HUNT, QUEST_CARRY = "QSPEAK", "QHUNT", "QCARRY"


class Character:
    def __init__(self):
        self.name = "Witcher"
        self.xp = 0
        self.passed_quests = set()
        self.taken_quests = set()


class Event:
    def __init__(self, kind):
        self.kind = kind


class NullHandler:
    def __init__(self, successor=None):
        self.__successor = successor  # next item in the chain

    def handle(self, char, event):
        if self.__successor:
            self.__successor.handle(char, event)


class QuestSpeak(NullHandler):
    def handle(self, char, event):
        if event.kind == QUEST_SPEAK:
            quest_name = "Talk to the farmer"
            xp = 100
            if quest_name not in (char.taken_quests | char.passed_quests):
                print("The Quest was taken.")
                char.taken_quests.add(quest_name)
            elif quest_name in char.taken_quests:
                print(f"{quest_name} was completed.")
                char.passed_quests.add(quest_name)
                char.taken_quests.remove(quest_name)
                char.xp += xp
        else:
            print("Pass the event further.")
            super().handle(char, event)


class QuestCarry(NullHandler):
    def handle(self, char, event):
        if event.kind == QUEST_CARRY:
            quest_name = "Carry the bucket of water to the village."
            xp = 100
            if quest_name not in (char.taken_quests | char.passed_quests):
                print("The Quest was taken.")
                char.taken_quests.add(quest_name)
            elif quest_name in char.taken_quests:
                print(f"{quest_name} was completed.")
                char.passed_quests.add(quest_name)
                char.taken_quests.remove(quest_name)
                char.xp += xp
        else:
            print("Pass the event further.")
            super().handle(char, event)


class QuestHunt(NullHandler):
    def handle(self, char, event):
        if event.kind == QUEST_HUNT:
            quest_name = "Hunt on dears in the forest"
            xp = 100
            if quest_name not in (char.taken_quests | char.passed_quests):
                print("The Quest was taken.")
                char.taken_quests.add(quest_name)
            elif quest_name in char.taken_quests:
                print(f"{quest_name} was completed.")
                char.passed_quests.add(quest_name)
                char.taken_quests.remove(quest_name)
                char.xp += xp
        else:
            print("Pass the event further.")
            super().handle(char, event)


class QuestGiver:
    def __init__(self):
        self.handlers = QuestCarry(QuestHunt(QuestSpeak(NullHandler())))
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def handle_events(self, char):
        for event in self.events:
            self.handlers.handle(char, event)


events = [Event(QUEST_CARRY), Event(QUEST_HUNT), Event(QUEST_SPEAK)]

quest_giver = QuestGiver()

for event in events:
    quest_giver.add_event(event)

player = Character()
quest_giver.handle_events(player)
