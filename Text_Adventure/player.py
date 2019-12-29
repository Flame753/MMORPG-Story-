import items
import world
import spells


class Player:
    def __init__(self):
        self.inventory = [items.Rock(),
                          items.Dagger(),
                          items.CrustyBread()]
        self.spell = [spells.FireBall(),
                      spells.IceBeam()]
        self.wearing = []

        self.x = world.start_tile_location[0]
        self.y = world.start_tile_location[1]
        self.maxHP = 100
        self.currentHP = 100
        self.maxmana = 100
        self.mana = 100
        self.strength = 1
        self.gold = 5
        self.victory = False

    def is_alive(self):
        return self.currentHP > 0

    def print_inventory(self):
        print("Inventory:")
        for item in self.inventory:
            print('* ' + str(item))
        print("Gold: {}".format(self.gold))

    def most_powerful_weapon(self):
        max_damage = 0
        best_weapon = None
        for item in self.inventory:
            try:
                if item.damage > max_damage:
                    best_weapon = item
                    max_damage = item.damage
            except AttributeError:
                pass
        return best_weapon

    def most_protective_armor(self):
        max_protection = 0
        best_armor = None
        for item in self.inventory:
            try:
                if item.protection > max_protection:
                    best_armor = item
                    max_protection = item.protection
            except AttributeError:
                pass
        return best_armor

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)

    def attack(self):
        try:
            best_weapon = self.most_powerful_weapon()
            room = world.tile_at(self.x, self.y)
            enemy = room.enemy
            print("You use {} against {}!".format(best_weapon.name, enemy.name))
            enemy.hp -= best_weapon.damage
        except AttributeError:
            print("You use Fist against {}!".format(enemy.name))
            enemy.hp -= 1
        if not enemy.is_alive():
            print("You killed {}!".format(enemy.name))
        else:
            print("{} HP is {}.".format(enemy.name, enemy.hp))

    def spell_attack(self):
        if self.maxmana == self.mana:
            print("You feel like you can cast infinite amount of spells.")
        elif self.mana >= self.maxmana/2:
            print("You feel like you have about half of your mana left.")
        else:
            print("You feel like your are about out of mana.")

        for i, type in enumerate(self.spell, 1):
            print("{}: {}".format(i, type.name))

        valid = False
        while not valid:
            choice = input("")
            try:
                chosen_spell = self.spell[int(choice) - 1]  # gets the spell out of the spell known

                if self.mana > chosen_spell.mana:
                    self.mana -= chosen_spell.mana
                    room = world.tile_at(self.x, self.y)
                    enemy = room.enemy
                    print(chosen_spell.description)
                    enemy.hp -= chosen_spell.damage
                    if not enemy.is_alive():
                        print("You killed {}!".format(enemy.name))
                    else:
                        print("{} HP is {}.".format(enemy.name, enemy.hp))
                    valid = True
                else:
                    print("You don't have enough mana to cast {}".format(chosen_spell.name))
                    return

            except (ValueError, IndexError):
                print("Invalid choice, try again.")

    def heal(self):
        consumables = [item for item in self.inventory if isinstance(item, items.Consumable)]
        if not consumables:
            print("you don't have any items to heal you!")
            return

        print("Choose an item to use to heal: ")
        for i, item in enumerate(consumables, 1):
            print("{}. {}".format(i, item))

        print("Enter Q to exit. ")  # Displaying Cancel

        valid = False
        while not valid:
            choice = input("")
            try:
                if choice in ['Q', 'q']:  # A way to exit
                    return
                to_eat = consumables[int(choice) - 1]
                self.currentHP = min(self.maxHP, self.currentHP + to_eat.healing_value)
                self.inventory.remove(to_eat)
                print("Current HP: {}".format(self.currentHP))
                valid = True
            except(ValueError, IndexError):
                print("Invalid choice, try again.")

    def trade(self):
        room = world.tile_at(self.x, self.y)
        room.check_if_trade(self)

    def status(self):
        best_weapon = self.most_powerful_weapon()
        print("Your Stats: \nMax HP: {} \nCurrent HP: {}".format(self.maxHP, self.currentHP))
        print("Max Mana: {} \nCurrent Mana: {}".format(self.maxmana, self.mana))
        print("your best weapon is your {}".format(best_weapon))

    def investigate(self):
        room = world.tile_at(self.x, self.y)
        enemy = room.enemy
        print("Your looking over a {},".format(enemy.name))
        try:
            if not enemy.inventory:
                print("And found nothing.")
            else:
                for i in range(len(enemy.inventory)):
                    item = enemy.inventory.pop()
                    print("Found a {}".format(item))
                    self.inventory.append(item)
        except AttributeError:
            print("This {} has nothing on it.".format(enemy.name))


