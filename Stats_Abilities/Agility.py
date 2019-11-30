class Agility:
    def __init__(self):
        self.dodge = 0

    def set_dodge(self, dodge):
        self.dodge = dodge

    def get_dodge(self):
        return self.dodge

    def __str__(self):
        return "Dodge = {}".format(self.dodge)


if __name__ == '__main__':
    a = Agility()
    print(a)
