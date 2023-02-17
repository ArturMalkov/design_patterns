"""
Memento pattern - keep a memento of an object's state to return to that state.
Memento is a token/handle representing the system state. It lets us roll back to the state when the token was generated.
It may or may not directly expose state information.

Motivation:
- an object or system goes through changes (e.g. bank account get deposits and withdrawals)
- there are different ways to navigate those changes:
a) to record every change (Command) and teach a command to 'undo' itself
b) to simply have snapshots of the system (Memento)
"""


class Memento:  # bank account snapshot
    def __init__(self, balance):
        self.balance = balance


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return Memento(self.balance)

    def restore(self, memento):
        self.balance = memento.balance

    def __str__(self):
        return f'Balance = {self.balance}'


if __name__ == '__main__':
    ba = BankAccount(100)
    m1 = ba.deposit(50)
    m2 = ba.deposit(25)
    print(ba)

    # restore to m1
    ba.restore(m1)
    print(ba)

    # restore to m2
    ba.restore(m2)
    print(ba)
