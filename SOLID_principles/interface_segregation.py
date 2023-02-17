"""
Don't want to put too many elements into an interface (class/method, etc.) (avoid 'general-purpose' interface).
Making interfaces which feature too many elements is not a good idea because you're forcing your clients to define
methods which they might not even need.

Many single-purpose interfaces are better than one general-purpose interface (i.e. the one which tries to cover too many
use-cases).

This principle is mainly about a problem of having a wrong interface which we force on to multiple classes.

Below - ordinary printer doesn't need to define fax and scan methods.
Split into the smallest interfaces possible so that people don't implement more than they need to.
YAGNI - you ain't going to need it.

Modularity of interfaces - low coupling - each interface shall solve a particular problem.
Super (very general) interface is an anti-pattern.
Favor decoupling over coupling!
Example - microservices architecture.
"""
from abc import abstractmethod


class Machine:  # you need to split this interface into several parts (3 parts)
    def print(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError


class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass


class OldFashionedPrinter(Machine):  # don't do this
    def print(self, document):
        # ok
        pass

    def fax(self, document):  # we need to specify these methods since they are present in the interface
        pass  # no operation

    def scan(self, document):  # the same comment as above - even though we don't need these methods for the old printer
        """Not supported!"""
        raise NotImplementedError("Printer cannot scan!")


# INSTEAD #

class Printer:  # we split the 3 interfaces into separate classes and inherit from them, when necessary
    @abstractmethod
    def print(self, document):
        pass


class Scanner:
    @abstractmethod
    def scan(self, document):
        pass


class MyPrinter(Printer):
    def print(self, document):
        print(document)


class Photocopier(Printer, Scanner):
    def print(self, document):
        pass

    def scan(self, document):
        pass


class MultiFunctionDevice(Printer, Scanner):  # if you want to have that interface available to users
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass


class MultiFunctionMachine(MultiFunctionDevice):
    def __init__(self, printer, scanner):
        self.printer = printer
        self.scanner = scanner

    def print(self, document):
        self.printer.print(document)

    def scan(self, document):
        self.scanner.scan(document)
