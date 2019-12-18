def food(agr):
    food_list = list()
    for x in range(agr):
        food_list.append(input("What is your favorite food? "))
    return food_list


def middle_item(lis):
    length = len(lis) / 2
    print(length)
    return lis[length]


def fav():
    favorites = []
    more_items = True
    while more_items:
        user_input = input("Enter something you like: ")
        if user_input == "":
            more_items = False
        else:
            favorites.append(user_input)
    print("here are all the things you like!")
    pretty_print_ordered(favorites)


def pretty_print_unordered(to_print):
    for item in to_print:
        print("* " + str(item))


def pretty_print_ordered(to_print):
    for i, value in enumerate(to_print, 1):
        print(str(i) + ". " + str(value))


fav()
# print(food(3))
# plants = ['Mercury', 'Venus', 'Earth', 2]
# print(middle_item(plants))
