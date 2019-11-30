from Attributes.Stats import Stats


class Character(Stats):
    def __init__(self, vitality=10, strength=10, defense=10, magic=10, agility=10):
        super().__init__(vitality, strength, defense, magic, agility)
        self.level = 1
        self.exp = 0

    def level_up(self):
        self.level += 1

    def get_level(self):
        return self.level

    def add_exp(self, exp):
        self.exp += exp

    def get_exp(self):
        return self.exp





if __name__ == '__main__':
    # print(help(Character()))
    char1 = Character()
    char1.add_exp(2)
    print(char1.get_exp())
    # print(char1.get_stats())
    print(char1)

