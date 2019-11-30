class Strength:
    def __init__(self):
        self.miss_chance = 0
        self.damage = 1

    def set_miss_chance(self, miss_chance):
        self.miss_chance = miss_chance

    def get_miss_chance(self):
        return self.miss_chance

    def set_damage(self, damage):
        self.damage = damage

    def get_damage(self):
        return self.damage
