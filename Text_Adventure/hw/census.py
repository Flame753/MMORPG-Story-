class Person:
    def __init__(self, name, age, favorite_foods):
        self.age = age
        self.name = name
        self. favorite_food = favorite_foods

    def birth_year(self):
        return 2019 - self.age

    def __str__(self):
        return "Name: {} Age: {} Favorite Food: {}".format(self.name, str(self.age), str(self.favorite_food[0]))


people = [Person("Ed", 11, ["hotdogs", "jawbreakers"]),
          Person("Edd", 11, ["broccoli"]),
          Person("Eddy", 12, ["chunky puffs", "jawbreakers"])]

age_sum = 0
year_sum = 0
for person in people:
    age_sum = age_sum + person.age
    year_sum = year_sum + person.birth_year()

print("The average age is: " + str(age_sum / len(people)))
print("The average birth year is: " + str(int(year_sum / len(people))))
print("The people polled in this census were:")
for person in people:
    print(person)