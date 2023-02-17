"""
Combining builders.
Different facets (aspects) of an object can be built with different builders working in tandem via a base class
"""


class Person:
    def __init__(self):
        # address
        self.street_address = None
        self.postcode = None
        self.city = None
        # employment
        self.company_name = None
        self.position = None
        self.annual_income = None

    def __str__(self):
        return f"Address: {self.street_address}, {self.postcode}, {self.city}" \
               f"Employed at {self.company_name} as {self.position} earning {self.annual_income}"


class PersonBuilder:
    def __init__(self, person=Person()):  # initializing a blank person with nothing in it
        self.person = person

    @property
    def works(self):
        return PersonJobBuilder(self.person)  # simple interface for jumping from one builder to another

    @property
    def lives(self):
        return PersonAddressBuilder(self.person)

    def build(self):
        return self.person


class PersonJobBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def at(self, company_name):
        self.person.company_name = company_name
        return self

    def as_a(self, position):
        self.person.position = position
        return self

    def earning(self, annual_income):
        self.person.annual_income = annual_income
        return self


class PersonAddressBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def at(self, street_address):
        self.person.street_address = street_address
        return self

    def with_postcode(self, postcode):
        self.person.postcode = postcode
        return self

    def in_city(self, city):
        self.person.city = city
        return self


if __name__ == '__main__':
    pb = PersonBuilder()
    person = pb\
        .lives\
            .at("123 London Road")\
            .with_postcode("SW12BC")\
            .in_city("London")\
        .works\
            .at("Google")\
            .as_a("Engineer")\
            .earning(123_000)\
        .build()

    print(person)
