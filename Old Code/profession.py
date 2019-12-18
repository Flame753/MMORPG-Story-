import math
import random


class Profession(object):
    name = 'Commoner'
    hit_die = 8
    bab_multiplier = 1

    @staticmethod
    def random():
        profs = Profession.__subclasses__()
        return profs[random.randint(0, len(profs) - 1)]()

    def roll_hitdie(self):
        return random.randint(1, self.hit_die)

    def bab(self, level):
        return math.floor(level * self.bab_multiplier)


class Barbarian(Profession):
    def __init__(self):
        self.name = 'Barbarian'
        self.hit_die = 12


class Bard(Profession):
    def __init__(self):
        self.name = 'Bard'
        self.bab_multiplier = 0.75


class Cleric(Profession):
    def __init__(self):
        self.name = 'Cleric'
        self.bab_multiplier = 0.75


class Druid(Profession):
    def __init__(self):
        self.name = 'Druid'
        self.bab_multiplier = 0.75


class Fighter(Profession):
    def __init__(self):
        self.name = 'Fighter'
        self.hit_die = 10


class Monk(Profession):
    def __init__(self):
        self.name = 'Monk'
        self.bab_multiplier = 0.75


class Paladin(Profession):
    def __init__(self):
        self.name = 'Paladin'
        self.hit_die = 10


class Ranger(Profession):
    def __init__(self):
        self.name = 'Ranger'
        self.hit_die = 10


class Rogue(Profession):
    def __init__(self):
        self.name = 'Rogue'
        self.bab_multiplier = 0.75


class Sorcerer(Profession):
    def __init__(self):
        self.name = 'Sorcerer'
        self.hit_die = 6
        self.bab_multiplier = 0.5


class Wizard(Profession):
    def __init__(self):
        self.name = 'Wizard'
        self.hit_die = 6
        self.bab_multiplier = 0.5


if __name__ == '__main__':
    print(Profession.random().name)
