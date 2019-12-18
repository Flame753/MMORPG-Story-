class Food:
    def __init__(self, name, carbs, protein, fat):
        self.name = name
        self.carbs = carbs
        self.protein = protein
        self.fat = fat

    def calories(self):
        """Calculates the number of calories in the food"""
        carbs_calories = self.carbs * 4
        protein_calories = self.protein * 4
        fat_calories = self.fat * 9
        return carbs_calories + protein_calories + fat_calories


class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def calories(self):
        """Returns the total calories in the recipe"""
        food_list = 0
        for food in self.ingredients:
            food_list += food.calories()
        return food_list

    def __str__(self):
        return self.name


# item = Food("ice cream", 0, 0, 20)
# print(item.calories())


recipe = Recipe("pizza",
                [Food("Bread", 1, 0, 0),
                 Food("Cheese", 0, 1, 0),
                 Food("Ham", 0, 0, 1)])

recipe2 = Recipe("pizza",
                 [Food("Bread", 3, 0, 0),
                  Food("Cheese", 0, 4, 0),
                  Food("Ham", 0, 0, 6)])

recipe_list = [recipe, recipe2]
for i in recipe_list:
    print(i.calories())
