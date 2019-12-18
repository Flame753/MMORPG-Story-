import math
import profession
import races
import random


class Character(object):
    def __init__(self):
        self.name = None
        self.race = None
        self.level = 0
        self.profession = None
        self.ability_scores = {
            'str': 10,
            'dex': 10,
            'con': 10,
            'int': 10,
            'wis': 10,
            'cha': 10
        }
        self.hit_points = 0
        self.wounds = 0

    @staticmethod
    def roll_ability_score():
        rolls = []
        while len(rolls) < 4:
            rolls.append(random.randint(1, 6))
        rolls.sort()
        return sum(rolls[1:])

    @staticmethod
    def modifier(score):
        return int(math.floor((score - 10) / 2))

    @staticmethod
    def random(level=1):
        char = Character()
        char.race = races.Race.random()
        char.profession = profession.Profession.random()
        char.level = level
        char.hit_points = char.profession.hit_die

        for ability in char.ability_scores.keys():
            char.ability_scores[ability] = Character.roll_ability_score()
        for ability in char.race.ability_modifiers.keys():
            char.ability_scores[ability] += char.race.ability_modifiers[ability]

        if level > 1:
            for i in range(1, level):
                char.hit_points += int(char.profession.roll_hitdie() + Character.modifier(char.ability_scores['con']))
        return char


if __name__ == '__main__':
    char = Character.random()  # random.randint(1, 20))
    print('Class: {}'.format(char.profession.name))
    print('Race: {}'.format(char.race.name))
    print('Level: {}'.format(char.level))
    print('AC: {}'.format(10 + char.modifier(char.ability_scores['dex'])))
    print('BAB: {}'.format(char.profession.bab(char.level)))
    print('Hit Points: {}'.format(char.hit_points))
    print('Ability Scores:')
    for ability in ['str', 'dex', 'con', 'int', 'wis', 'cha']:
        print(
            '\t{}: {} ({})'.format(ability, char.ability_scores[ability], char.modifier(char.ability_scores[ability])))
