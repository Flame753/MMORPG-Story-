import math
import random
from StoryPieces import valid_anw, story_arc, paths, actions


if __name__ == "__main__":

    arc = story_arc()
    answer = input("Would you like to start the game? (yes/no)")
    if valid_anw(answer) == "yes":
        print("Your entering into a {}.".format(arc))
        print(f"Your are walking through this {arc} and see {3} paths to choose from.")

        answer = input("Which path do you choose? (right/left/straight)")
        chosen_path = paths(valid_anw(answer))
        print(chosen_path.format("box"))
        answer = input("What would you like to do? (run/fight/explore)")
        chosen_action = actions(valid_anw(answer))
    else:
        print("That is to bad")
