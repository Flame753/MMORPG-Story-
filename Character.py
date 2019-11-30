from Stats_Abilities.Stats import Stats


class Character(Stats):
    def __init__(self, vitality=0, strength=0, defense=0, magic=0, agility=0):
        super().__init__(vitality, strength, defense, magic, agility)
        self.level = 1
        self.exp = 0

    def set_level(self, level):
        self.level = level

    def get_level(self):
        return self.level

    def add_exp(self, exp):
        self.exp = self.exp + exp

    def get_exp(self):
        return self.exp


if __name__ == '__main__':
    # print(help(Character()))
    # char1 = Character(34,34,6,2,1)
    # print(char1.get_stats())
    # print(char1)
    print(help(Character))
