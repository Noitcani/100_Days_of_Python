from turtle import Turtle
import random
from time import sleep

COLORS = ["blue", "red", "pink", "brown", "purple", "indigo", "orange"]

# Starting from y = -250 to 250, 5 zones, 100y-px each

SPAWN_X = [-200, 900]
SPAWN_Y = {
    "zone1": [-13, -7],
    "zone2": [-7, -2],
    "zone3": [-2, 3],
    "zone4": [3, 8],
    "zone5": [8, 13]
}

all_cars = []


# Make a Car class
class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.ht()
        self.color(random.choice(COLORS))  # Random colors
        self.shape("square")
        self.shapesize(stretch_wid=0.8, stretch_len=2)
        self.setx(320)
        self.st()
        self.movespeed = -2

    # Cars move(level) left only, speedup by level
    def move(self, level):
        new_x = self.xcor() + (self.movespeed + (level * -0.8))
        self.goto(new_x, self.ycor())

    def spawn(self, spawn_x, spawn_y):
        new_car = Car()
        new_car.setpos(spawn_x, spawn_y)
        all_cars.append(new_car)

    def car_respawn(self, level):
        self.pu()
        self.ht()
        new_x = 320
        self.setpos(new_x, (random.randint(-13, 14))*20)
        self.st()
        self.move(level)

    # Car Spawner
    def spawner_run(self, level):
        # Set number of cars per zone, based on level
        for i in range(5 + int(level*.3)):
            for zone in SPAWN_Y.keys():
                spawn_x = random.randint(SPAWN_X[0], SPAWN_X[1])
                spawn_y = random.randint((SPAWN_Y[zone][0]), (SPAWN_Y[zone][1]))
                self.spawn(spawn_x, spawn_y*20)

# Some car_generator AI, radomly generates density based on ycor
# Total number of cars in each zone determined by level
# Breakdown by zones
# Breakdown by " row spawn point"
# Each row can either spawn or not spawn,
# If spawned, sleep_as cooldown, based on level
