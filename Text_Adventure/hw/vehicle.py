class Vehicle:
    def __init__(self):
        raise NotImplementedError("Not allowed, Don't make a Vehicle.")


class Motorcycle(Vehicle):
    def __init__(self):
        self.wheels = 2


class Car(Vehicle):
    def __init__(self):
        self.wheels = 4


print(Motorcycle())
