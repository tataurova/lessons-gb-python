class Bird:
    name = "UN"  # свойство
    distance = 0
    speed = 100

    def call(self):  # метод call
        this_name = self.name
        print("my name is " + this_name)

    def run(self, distance=False):
        if not distance:
            distance = self.speed
        self.distance = self.distance + distance

    def __init__(self, name, speed, steps):
        self.name = name
        self.speed = speed
        for n in range(steps):
            self.run()

'''
owl = Bird()
owl.name = "Owl"
owl.speed = 150


eagle = Bird()
eagle.name = "Eagle"
eagle.speed = 400

owl.run()
print(owl.distance)

eagle.run()
print(eagle.distance)
'''
owl = Bird("Owl", 150, 3)
eagle = Bird("Eaglr", 300, 1)

print(owl.name, eagle.name)
print(owl.distance, eagle.distance)
