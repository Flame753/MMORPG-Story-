import math
import random
import StoryPieces


if __name__ == "__main__":

    arc = StoryPieces.story_arc()
    answer = input("Would you like to start the game? (yes/no)")
    print(dir(answer))
    if StoryPieces.valid_anw(answer) == "yes":
        print("Your entering into a {}.".format(arc))
        print("you are walking through")
    else:
        print("That is to bad")
