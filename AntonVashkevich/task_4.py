class Bird:
    def __init__(self, name):
        self.name = name


    def fly(self):
        print(f"{self.name} bird can fly")

    def walk(self):
        print(f"{self.name} bird can walk")

    def __repr__(self):
        return f"{self.name} bird can fly and walk"


class FlyingBird(Bird):
    def __init__(self, name, ration="grains"):

        super().__init__(name)
        self.ration = ration

    def eat(self):
        print(f"It eats mostly {self.ration}")

    def __repr__(self):
        return f"{self.name} bird can eat, fly and walk"


class NonFlyingBird(Bird):

    def __init__(self, name, ration="fish"):

        super().__init__(name)
        self.ration = ration

    def eat(self):
        print(f"It eats {self.ration}")

    def fly(self):
        raise AttributeError(f"{self.name} object has no attribute 'fly'")

    def swim(self):
        print(f"{self.name} bird can swim")

    def __repr__(self):
        return f"{self.name} bird can eat, swim and walk"


class SuperBird(FlyingBird, NonFlyingBird):
    def __init__(self, name, ration="all"):
        NonFlyingBird.__init__(self, name, ration)

    def fly(self):
        FlyingBird.fly(self)

    def __repr__(self):
        return f"{self.name} bird can eat, fly, swim and walk"

