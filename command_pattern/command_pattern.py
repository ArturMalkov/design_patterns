"""
Command pattern is an object which represents an instruction to perform a particular action. It contains all the information
necessary for the action to be taken.

Encapsulates a request (i.e. the 'command' itself) as an object thereby letting you parametrize other objects with
different requests, queue or log requests and support undo (i.e. 'rollback' or inverse of itself) operations.

Example: we attach a command (e.g. turn on the light) to the Invoker (e.g. remote controller) and the operation, when it is executed (when a
particular button on a remote controller is pressed), does smth to a Receiver (e.g. smart device).
Each command has 'do'/'execute' and 'undo'/'unexecute' methods.

Very often used in GUI commands in text editors (multi-level undo/redo)

Motivation:
- to undo certain operations
- to keep track/record of operations (serialize a sequence of operations)

It is also possible to create composite commands (aka macros)
Part of command-query separation.
"""

import unittest
from abc import ABC, abstractmethod
from enum import Enum


class BankAccount:
    OVERDRAFT_LIMIT = -500

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. Balance: ${self.balance}")

    def withdraw(self, amount):
        if self.balance - amount >= BankAccount.OVERDRAFT_LIMIT:
            self.balance -= amount
            print(f"Withdrew ${amount}. Balance: ${self.balance}")
            return True
        return False

    def __str__(self):
        return f"Balance: ${self.balance}"


class Command(ABC):
    def __init__(self):
        self.success = False

    @abstractmethod
    def invoke(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class BankAccountCommand(Command):
    class Action(Enum):
        DEPOSIT = 0
        WITHDRAW = 1

    def __init__(self, account, action, amount):
        super().__init__()
        self.account = account
        self.action = action
        self.amount = amount
        self.success = None

    def invoke(self):
        if self.action == self.Action.DEPOSIT:
            self.account.deposit(self.amount)
        elif self.action == self.Action.WITHDRAW:
            self.success = self.account.withdraw(self.amount)

    def undo(self):
        if not self.success:
            return

        if self.action == self.Action.DEPOSIT:
            self.account.withdraw(self.amount)
        elif self.action == self.Action.WITHDRAW:
            self.account.deposit(self.amount)


class CompositeBankAccountCommand(Command, list):  # Composite command is a variation of command pattern!
    def __init__(self, items):
        super().__init__()
        for item in items:
            self.append(item)

    def invoke(self):
        for command in self:
            command.invoke()

    def undo(self):
        for command in reversed(self):
            command.undo()


class MoneyTransferCommand(CompositeBankAccountCommand):
    def __init__(self, from_acct, to_acct, amount):
        super().__init__([
            BankAccountCommand(from_acct,
                               BankAccountCommand.Action.WITHDRAW,
                               amount),
            BankAccountCommand(to_acct,
                               BankAccountCommand.Action.DEPOSIT,
                               amount)
        ])

    def invoke(self):
        ok = True
        for command in self:
            if ok:
                command.invoke()
                ok = command.success
            else:
                command.success = False
        self.success = ok


class TestSuite(unittest.TestCase):
    def test_composite_deposit(self):
        ba = BankAccount()
        deposit1 = BankAccountCommand(ba, BankAccountCommand.Action.DEPOSIT, 100)
        deposit2 = BankAccountCommand(ba, BankAccountCommand.Action.DEPOSIT, 50)
        composite_command = CompositeBankAccountCommand([deposit1, deposit2])
        composite_command.invoke()
        print(ba)
        composite_command.undo()
        print(ba)

    def test_transfer_fail(self):
        ba1 = BankAccount(100)
        ba2 = BankAccount()

        amount = 1000
        withdrawal_command = BankAccountCommand(ba1, BankAccountCommand.Action.WITHDRAW, amount)
        deposit_command = BankAccountCommand(ba2, BankAccountCommand.Action.DEPOSIT, amount)
        transfer = CompositeBankAccountCommand([withdrawal_command, deposit_command])
        print("-------------------")
        transfer.invoke()
        print(f"ba1: {ba1}, ba2: {ba2}")
        transfer.undo()
        print(f"ba1: {ba1}, ba2: {ba2}")

    def test_better_transfer(self):
        ba1 = BankAccount(100)
        ba2 = BankAccount()

        amount = 5000

        transfer = MoneyTransferCommand(ba1, ba2, amount)
        transfer.invoke()
        print(f"ba1: {ba1}, ba2: {ba2}")
        transfer.undo()
        print(f"ba1: {ba1}, ba2: {ba2}")
        print(transfer.success)


if __name__ == "__main__":
    bank_account = BankAccount()  # 0
    cmd = BankAccountCommand(
        bank_account,
        BankAccountCommand.Action.DEPOSIT,
        200
    )
    cmd.invoke()
    print(f"After $200 deposit: {bank_account}")

    cmd.undo()
    print(f"$200 deposit undone: {bank_account}")

    illegal_cmd = BankAccountCommand(
        bank_account,
        BankAccountCommand.Action.WITHDRAW,
        1000
    )
    illegal_cmd.invoke()
    print(f"After impossible withdrawal: {bank_account}")
    illegal_cmd.undo()

    unittest.main()
