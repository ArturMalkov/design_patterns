"""
'Undo'/'redo' operations implemented with memento
"""


class Memento:  # bank account snapshot
    def __init__(self, balance):
        self.balance = balance


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.changes = [Memento(self.balance)]
        self.current = 0  # where we are in the list of mementos (to enable "undo" and "redo" operations)

    def deposit(self, amount):
        self.balance += amount
        memento = Memento(self.balance)
        self.changes.append(memento)
        self.current += 1
        return memento

    def restore(self, memento):
        if memento:
            self.balance = memento.balance
            self.changes.append(memento)
            self.current = len(self.changes) - 1

    def undo(self):
        if self.current > 0:
            self.current -= 1
            memento = self.changes[self.current]
            self.balance = memento.balance
            return memento
        return None  # nothing to undo

    def redo(self):
        if self.current + 1 < len(self.changes):  # cannot redo if already in the last position
            self.current += 1
            memento = self.changes[self.current]
            self.balance = memento.balance
            return memento
        return None

    def __str__(self):
        return f"Balance = {self.balance}"


if __name__ == "__main__":
    account = BankAccount(100)
    account.deposit(50)
    account.deposit(25)
    print(account)

    account.undo()
    print(account)
    account.undo()
    print(account)
    account.redo()
    print(account)
