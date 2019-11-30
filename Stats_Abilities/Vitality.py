class Vitality:
    def __init__(self):
        self.health = 1
        self.wounds = 0
        self.regeneration = 1

    def set_health(self, health):
        self.health = health

    def get_health(self):
        return self.health

    def set_wounds(self, wounds):
        self.wounds = wounds

    def get_wounds(self):
        return self.wounds

    def set_regeneration(self, regeneration):
        self.regeneration = regeneration

    def get_regeneration(self):
        return self.regeneration
