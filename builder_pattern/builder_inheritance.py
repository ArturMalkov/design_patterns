class Person:
    def __init__(self):
        self.name = None
        self.position = None
        self.date_of_birth = None

    def __str__(self):
        return f"{self.name} born on {self.date_of_birth} " \
               f"works as {self.position}"

    @staticmethod
    def new():
        return PersonBuilder()


class PersonBuilder:  # adding new builders is possible via further inheritance - in line with open-closed principle
    def __init__(self):
        self.person = Person()

    def build(self):
        return self.person


class PersonInfoBuilder(PersonBuilder):
    def called(self, name):
        self.person.name = name
        return self  # use 'self' to chain method calls together (to make builder fluent)


class PersonJobBuilder(PersonInfoBuilder):
    def works_as_a(self, position):
        self.person.position = position
        return self


class PersonBirthDateBuilder(PersonJobBuilder):
    def born(self, date_of_birth):
        self.person.date_of_birth = date_of_birth
        return self


if __name__ == "__main__":
    pb = PersonBirthDateBuilder()
    me = pb\
        .called("Artur")\
        .works_as_a("Quant")\
        .born("18/08/1992")\
        .build()

    print(me)
