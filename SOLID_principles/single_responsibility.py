"""
Single Responsibility or Separation of Concerns
A class should only have one reason to change / axis of change.
Class' attributes and methods should be devoted to one concern (e.g. business area segment) only.
(responsibility is about a group of tasks connected to the same feature/business area segment, but not a single task)

Don't overload your objects with too many responsibilities - different classes handling different, independent tasks/problems.
Anti-pattern - God-object (which does everything)

Decomposition/modularity allows us to:
- ensure right encapsulation (easier testing, VCS, simultaneous work of multiple developers)
- avoid high coupling - when if smth breaks, other parts break as well
- improve readability, maintainability and scaling of code

Uncle Bob (Robert Martin) - a module/class/etc. should have a single reason to change and it must be fully encapsulated
within that class.
"""


class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count}: {text}")

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)

    # def save(self, filename):
    #     file = open(filename, 'w')
    #     file.write(str(self))
    #     file.close()
    #
    # def load(self, filename):
    #     pass
    #
    # def load_from_web(self, uri):
    #     pass


class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        with open(filename, 'w') as file:
            file.write(str(journal))
