import random
import character


class Monsters(object):
    def __init__(self):
        self.name = 'Unknown'
        self.CR = None
        self.xp = 0
        self.AC = 0
        self.attack = {}
        self.ability_scores = {}
        self.hit_points = 0
        self.base_hit_points = {}
        self.wounds = 0

    @staticmethod
    def random():
        monsters = Monsters.__subclasses__()
        return monsters[random.randint(0, len(monsters) - 1)]()

    # @staticmethod
    # def damageDealt():
    #     mons = Monsters()
    #     score = character.modifier(mons.ability_scores(mons.damageDie[3]))
    #     for x in range(mons.damageDie[1]):
    #         damage = random.randint(1, mons.damageDie[2]) + score
    #     return damage

    @staticmethod
    def calc_hit_points():
        return

class Skunk(Monsters):
    def __init__(self):
        super().__init__()
        self.name = 'Skunk'
        self.CR = 1/8
        self.xp = 50
        self.AC = 13
        self.attack = {"bite": {"many_attack": 1, "hit": 3, "number_of_dice": 1, "size_of_dice": 3, "damage": -4}}
        self.ability_scores = {'str': 3, 'dex': 15, 'con': 9, 'int': 2, 'wis': 12, 'cha': 6}
        self.base_hit_points = {"average_health": 4, "number_of_dice": 1, "size_of_dice": 8, "health": 0}


class Fox(Monsters):
    def __init__(self):
        super().__init__()
        self.name = 'Fox'
        self.CR = 1/4
        self.xp = 100
        self.AC = 14
        self.attack = {"bite": {"many_attack": 1, "hit": 1, "number_of_dice": 1, "size_of_dice": 3, "damage": -1}}
        self.ability_scores = {'str': 9, 'dex': 15, 'con': 13, 'int': 2, 'wis': 12, 'cha': 6}
        self.base_hit_points = {"average_health": 5, "number_of_dice": 1, "size_of_dice": 8, "health": 1}


class GiantSkunk(Monsters):
    def __init__(self):
        super().__init__()
        self.name = 'Skunk'
        self.CR = 1/4
        self.xp = 100
        self.AC = 14
        self.attack = {"bite": {"many_attack": 1, "hit": 4, "number_of_dice": 1, "size_of_dice": 3, "damage": -4},
                       "claws": {"many_attack": 2, "hit": 4, "number_of_dice": 1, "size_of_dice": 2, "damage": -4}}
        self.ability_scores = {'str': 3, 'dex': 15, 'con': 9, 'int': 2, 'wis': 12, 'cha': 6}
        self.base_hit_points = {"average_health": 5, "number_of_dice": 1, "size_of_dice": 8, "health": -1}


class Boar(Monsters):
    def __init__(self):
        super().__init__()
        self.name = 'Boar'
        self.CR = 2
        self.xp = 600
        self.AC = 14
        self.attack = {"gore": {"many_attack": 1, "hit": 4, "number_of_dice": 1, "size_of_dice": 8, "damage": 4}}
        self.ability_scores = {'str': 17, 'dex': 10, 'con': 17, 'int': 2, 'wis': 13, 'cha': 4}
        self.base_hit_points = {"average_health": 18, "number_of_dice": 2, "size_of_dice": 8, "health": 9}

