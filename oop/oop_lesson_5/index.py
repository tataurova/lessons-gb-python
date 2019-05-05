from birds import Bird


class Chicken(Bird):
    type = "chicken"

    def __init__(self, steps):
        self.name = "Chicken"
        self.speed = 50
        for n in range(steps):
            self.run()


owl = Bird("Owl", 150, 3)
eagle = Bird("Eagle", 300, 1)
chicken = Chicken(10)
chicken2 = Chicken(100)
print(chicken.type)

print(owl.name, eagle.name, chicken.name, chicken2.name)
print(owl.distance, eagle.distance, chicken.distance, chicken2.distance)


