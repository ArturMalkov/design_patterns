class Creature:
    _strength = 0
    _agility = 1
    _intelligence = 2

    def __init__(self):
        # self.strength = 10  # commented out is very unstable
        # self.agility = 10
        # self.intelligence = 10
        self.stats = [10, 10, 10]  # enables iteration on attributes

    @property
    def strength(self):
        return self.stats[Creature._strength]

    @strength.setter
    def strength(self, value):
        self.stats[Creature._strength] = value

    @property
    def agility(self):
        return self.stats[Creature._agility]

    @agility.setter
    def agility(self, value):
        self.stats[Creature._agility] = value

    @property
    def intelligence(self):
        return self.stats[Creature._intelligence]

    @intelligence.setter
    def intelligence(self, value):
        self.stats[Creature._intelligence] = value

    @property
    def sum_of_stats(self):
        return sum(self.stats)
        # return self.strength + self.agility + self.intelligence

    @property
    def max_stat(self):
        return max(self.stats)
        # return max(self.strength, self.agility, self.intelligence)

    @property
    def average_stat(self):
        return float(self.sum_of_stats) / len(self.stats)
        # return self.sum_of_stats / 3.0
