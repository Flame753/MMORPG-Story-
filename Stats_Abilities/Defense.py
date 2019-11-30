class Defense:
    def __init__(self):
        self.damage_resistance = 0

    def set_damage_resistance(self, damage_resistance):
        self.damage_resistance = damage_resistance

    def get_damage_resistance(self):
        return self.damage_resistance

    def __str__(self):
        return "damage_resistance = {} ".format(self.damage_resistance)


if __name__ == '__main__':
    a = Defense()
    print(a)