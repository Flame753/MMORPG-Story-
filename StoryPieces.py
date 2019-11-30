import math
import random


def valid_anw(string):
    return string.lower().strip()


def story_arc():
    switcher = {
        1: "Forest",
        2: "Dungeon",
        3: "Town"
    }
    return switcher.get(random.randint(1, 3), "Problem has occurred check your code!")


def paths(arg):
    switcher = {
        "right": "You turned right and you see a {} up a head.",
        "left": "You turned left and you see a {} up a head.",
        "straight": "You went straight and you see a {} up a head."
    }
    return switcher.get(arg, "Not a valid option")


def actions(arg):
    switcher = {
        "run": "",
        "fight": "",
        "explore": "",
    }
    return switcher.get(arg, "Your unable to do that action.")



