"""
Monostate - a variation of Singleton pattern.
Whenever you're initializing the object of the class CEO, you're actually referring to the same set of attributes
"""


class CEO:
    __shared_state = {
        "name": "Steve",
        "age": 55
    }

    def __init__(self):
        self.__dict__ = self.__shared_state

    def __str__(self):
        return f"{self.name} is {self.age} years old."


ceo1 = CEO()
print(ceo1)
ceo2 = CEO()
print(ceo2)


# More generic approach


class Monostate:
    _shared_state = {
        "name": "Steve",
        "age": 55
    }

    def __new__(cls, *args, **kwargs):
        obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj


class CFO(Monostate):
    def __init__(self):
        self.name = ""
        self.money_managed = 0

    def __str__(self):
        return f"{self.name} manages ${self.money_managed}"


cfo1 = CFO()
cfo1.name = "Cheryl"
cfo1.money_managed = 100
print(cfo1)

cfo2 = CFO()
cfo2.name = "Ruth"
cfo2.money_managed = 10
print(cfo2)
print(cfo1)
