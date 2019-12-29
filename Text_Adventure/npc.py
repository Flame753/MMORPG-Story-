import items


class NonPlayableCharacter():
    def __init__(self):
        raise NotImplementedError("Do not create raw NPC objects.")

    def __str__(self):
        return self.name


class Trader(NonPlayableCharacter):
    def __init__(self):
        self.name = "Trader"
        self.gold = 100
        self.inventory = [items.CrustyBread(),
                          items.CrustyBread(),
                          items.CrustyBread(),
                          items.HealingPotion(),
                          items.HealingPotion()]


class Blacksmith(NonPlayableCharacter):
    def __init__(self):
        self.name = "Blacksmith"
        self.gold = 200
        self.inventory = [items.IronSword(), items.LeatherArmor()]