from Stats_Abilities import Stats
import Stats_Abilities


class Character:
    def __init__(self):
        self.stats = Stats_Abilities.Stats
        self.level = 1
        self.exp = 0

    def set_stats(self, stats):
        self.stats = self.stats + stats

    def get_stats(self):
        return self.stats

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
