from abc import ABC, abstractmethod
from enum import Enum, auto


class HotDrink(ABC):
    @abstractmethod
    def consume(self):
        pass


class Tea(HotDrink):
    def consume(self):
        print("This tea is delicious!")


class Coffee(HotDrink):
    def consume(self):
        print("This coffee is delicious")


class HotDrinkFactory(ABC):
    @abstractmethod
    def prepare(self, amount):
        pass


class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f"Put in tea bag, boil water, pour {amount}ml, enjoy!")
        return Tea()


class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f"Grind some beans, boil water, pour {amount}ml, enjoy!")
        return Coffee()


# def make_drink(type_):
#     if type_ == "tea":
#         return TeaFactory().prepare(200)
#     elif type_ == "coffee":
#         return CoffeeFactory().prepare(50)
#     else:
#         return None


class HotDrinkMachine:
    class AvailableDrink(Enum):
        TEA = auto()
        COFFEE = auto()

    factories = []
    initialized = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            for d in self.AvailableDrink:
                name = d.name[0] + d.name[1:].lower()
                factory_name = name + "Factory"
                factory_instance = eval(factory_name)()
                self.factories.append((name, factory_instance))

    def make_drink(self):
        print("Available drinks:")
        for f in self.factories:
            print(f[0])

        choice = int(input(f"Please pick a drink: 0-{len(self.factories)-1}: "))
        amount = int(input("Please specify amount: "))
        return self.factories[choice][1].prepare(amount)


if __name__ == "__main__":
    # entry = input("What kind of drink would you like? ")
    # drink = make_drink(entry)
    # drink.consume()
    drink_machine = HotDrinkMachine()
    drink_machine.make_drink()
