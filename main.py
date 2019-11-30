import math
import random
import StoryPieces


if __name__ == "__main__":

    arc = StoryPieces.story_arc()
    answer = input("Would you like to start the game? (yes/no)")
    if StoryPieces.valid_anw(answer) == "yes":
        print("Your entering into a {}.".format(arc))
        print("Your are walking through this {} and ".format(arc))
    else:
        print("That is to bad")
