import random
import character


class Monsters(object):
    def __init__(self):
        self.name = 'Unknown'
        self.xp = 0
        self.bab = 0
        self.damageDie = 0
        self.ability_scores = {}
        self.hit_points = 0
        self.wounds = 0

    @staticmethod
    def random():
        monsters = Monsters.__subclasses__()
        return monsters[random.randint(0, len(monsters) - 1)]()

    @staticmethod
    def damageDealt():
        mons = Monsters()
        score = character.modifier(mons.ability_scores(mons.damageDie[3]))
        for x in range(mons.damageDie[1]):
            damage = random.randint(1, mons.damageDie[2]) + score
        return damage


class Boar(Monsters):
    def __init__(self):
        super().__init__()
        self.name = 'Boar'
        self.xp = 600
        self.bab = 1
        self.damageDie = [1, 8, 'str']
        self.ability_scores = {'str': 17, 'dex': 10, 'con': 17, 'int': 2, 'wis': 13, 'cha': 4}
        elf.hit_points = [2, 8, 9]


mons = Monsters()
print('damage: {}'.format(mons.damageDealt()))
