import random


class Race(object):
    def __init__(self):
        self.name = 'Unknown'
        self.ability_modifiers = {}

    @staticmethod
    def random():
        races = Race.__subclasses__()
        return races[random.randint(0, len(races) - 1)]()


class Dwarf(Race):
    def __init__(self):
        super().__init__()
        self.name = 'Dwarf'
        self.ability_modifiers = {'con': 2, 'wis': 2, 'cha': -2}


class Elf(Race):
    def __init__(self):
        super().__init__()
        self.name = 'Elf'
        self.ability_modifiers = {'dex': 2, 'int': 2, 'con': -2}


class Gnome(Race):
    def __init__(self):
        super().__init__()
        self.name = 'Gnome'
        self.ability_modifiers = {'con': 2, 'cha': 2, 'str': -2}


class HalfElf(Race):
    def __init__(self):
        super().__init__()
        self.name = 'Half-Elf'
        random_ability = random.choice(['str', 'dex', 'con', 'int', 'wis', 'cha'])
        self.ability_modifiers = {random_ability: 2}


class HalfOrc(Race):
    def __init__(self):
        super().__init__()
        self.name = 'Half-Orc'
        random_ability = random.choice(['str', 'dex', 'con', 'int', 'wis', 'cha'])
        self.ability_modifiers = {random_ability: 2}


class Halfling(Race):
    def __init__(self):
        super().__init__()
        self.name = 'Halfling'
        self.ability_modifiers = {'dex': 2, 'cha': 2, 'str': -2}


class Human(Race):
    def __init__(self):
        super().__init__()
        self.name = 'Human'
        random_ability = random.choice(['str', 'dex', 'con', 'int', 'wis', 'cha'])
        self.ability_modifiers = {random_ability: 2}
