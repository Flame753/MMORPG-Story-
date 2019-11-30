from Attributes.Vitality import Vitality
from Attributes.Magic import Magic
from Attributes.Defense import Defense
from Attributes.Agility import Agility
from Attributes.Strength import Strength


class Stats(Vitality, Magic, Defense, Agility, Strength):
    def __init__(self, vitality=0, strength=0, defense=0, magic=0, agility=0):
        Vitality.__init__(self)
        Magic.__init__(self)
        Defense.__init__(self)
        Agility.__init__(self)
        Strength.__init__(self)

        self.vitality = vitality
        self.strength = strength
        self.defense = defense
        self.magic = magic
        self.agility = agility

    def set_vitality(self, vitality):
        self.vitality = vitality

    def get_vitality(self):
        return self.vitality

    def set_strength(self, strength):
        self.strength = strength

    def get_strength(self):
        return self.strength

    def set_defense(self, defense):
        self.defense = defense

    def get_defense(self):
        return self.defense

    def set_magic(self, magic):
        self.magic = magic

    def get_magic(self):
        return self.magic

    def set_agility(self, agility):
        self.agility = agility

    def get_agility(self):
        return self.agility

    def get_stats(self):
        return {"vitality": self.vitality,
                "strength": self.strength,
                "defense": self.defense,
                "magic": self.magic,
                "agility": self.agility}

    def __str__(self):
        return f"vitality = {self.vitality} \n" \
               f"strength = {self.strength} \n" \
               f"defense = {self.defense} \n" \
               f"magic = {self.magic} \n" \
               f"agility = {self.agility} "


if __name__ == '__main__':
    # st1 = Stats(5,5,2,6)
    # print(Stats.get_stats(st1))
    print(help(Stats))

