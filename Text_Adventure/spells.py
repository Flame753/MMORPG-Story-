class Spell:
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon Objects.")

    def __str__(self):
        return self.name


class FireBall(Spell):
    def __init__(self):
        self.name = "Fire Ball"
        self.damage = 75
        self.mana = 50
        self.description = "You shot a Fire Ball out of your hand and burns the enemy alive."


class IceBeam(Spell):
    def __init__(self):
        self.name = "Ice Beam"
        self.damage = 15
        self.mana = 20
        self.description = "You shot a Ice Beam our of your hand and freeze your target"


