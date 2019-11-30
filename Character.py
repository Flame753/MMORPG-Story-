from Stats_Abilities import Stats


starting_stats = Stats
class Character:
    def __init__(self):
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
    char1 = Character()
    print(Character)