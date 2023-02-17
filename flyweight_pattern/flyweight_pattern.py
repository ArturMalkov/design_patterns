"""
Flyweight design pattern - a space optimization technique that lets us use less memory by storing externally
the data associated with similar objects.

Motivation:
- avoid redundancy when storing data:
e.g. MMORPG has plenty of users with identical first/last names - there's no sense in storing same first/last name
over and over again.
-> instead, store a list of names and references to them.

e.g. bold or italic text formatting - we don't want each character to have a formatting character
-> instead, operate on ranges (e.g. line number, start/end positions)

Implementation:
- store common data (intrinsic state) externally
- specify an index or a reference into the external data store
- define the idea of "ranges" on homogeneous collections and store data related to those ranges
"""
import string
import random


class User:
    def __init__(self, name):
        self.name = name  # inefficient


class User2:
    strings = []

    def __init__(self, full_name):  # format: first_name last_name
        def get_or_add(s):  # storing indices to parts of the string
            if s in self.strings:
                return self.strings.index(s)
            else:
                self.strings.append(s)
                return len(self.strings) - 1
        self.names = [get_or_add(x) for x in full_name.split(" ")]

    def __str__(self):
        return " ".join([self.strings[x] for x in self.names])


def random_string():
    chars = string.ascii_lowercase
    return "".join(
        [random.choice(chars) for x in range(8)]
    )


if __name__ == "__main__":
    users = []

    first_names = [random_string() for x in range(100)]
    last_names = [random_string() for x in range(100)]

    for first in first_names:  # calculating Cartesian product - set of ordered first-last name pairs
        for last in last_names:
            users.append(User2(f"{first} {last}"))

    print(users[0])
