import turtle as t
import random

import colorgram

my_turtle = t.Turtle()
screen = t.Screen()
t.colormode(255)
t.setup(550, 550)

colors = colorgram.extract('colorpalettebase.jpg', 10)


def random_color():
    r = colors[random.randint(0, 9)].rgb[0]
    g = colors[random.randint(0, 9)].rgb[1]
    b = colors[random.randint(0, 9)].rgb[2]
    return r, g, b


my_turtle.width(2)
my_turtle.speed(0)
heading = 0

my_turtle.ht()
my_turtle.pu()
y_coord = -225

for y in range(10):
    my_turtle.setposition(-225, y_coord)
    for i in range(10):
        my_turtle.dot(20, random_color())
        my_turtle.fd(50)
    y_coord += 50



screen.exitonclick()