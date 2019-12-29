class Weapon:
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon Objects.")

    def __str__(self):
        return self.name


class Rock(Weapon):
    def __init__(self):
        self.name = "Rock"
        self.description = "A fist-sized rock, suitable for bludgeoning."
        self.damage = 5
        self.value = 1


class Dagger(Weapon):
    def __init__(self):
        self.name = "Dagger"
        self.description = "A small dagger with some rust." \
                           "Somewhat more dangerous than a rock."
        self.damage = 10
        self.value = 20


class RustySword(Weapon):
    def __init__(self):
        self.name = "Rusty Sword"
        self.description = "This sword is showing its age, " \
                           "but still has some fight in it."
        self.damage = 25
        self.value = 100


class IronSword(Weapon):
    def __init__(self):
        self.name = "Iron Sword"
        self.description = "This sword is very sharpe, and" \
                           "forged with the finest iron that money can buy."
        self.damage = 40
        self.value = 150


class Consumable:
    def __init__(self):
        raise NotImplementedError("Do not create raw Consumable objects.")

    def __str__(self):
        return "{} (+{} HP)".format(self.name, self.healing_value)


class CrustyBread(Consumable):
    def __init__(self):
        self.name = "Crusty Bread"
        self.healing_value = 10
        self.value = 12


class HealingPotion(Consumable):
    def __init__(self):
        self.name = "Health Potion"
        self.healing_value = 50
        self.value = 60


class Armor:
    def __init__(self):
        raise NotImplementedError("Do not create raw Armor objects.")

    def __str__(self):
        return self.name


class LeatherArmor(Armor):
    def __init__(self):
        self.name = "Leather Armor"
        self.description = "This leather is showing its age, " \
                           "but still has some hits it's can take."
        self.protection = .1
        self.value = 75
