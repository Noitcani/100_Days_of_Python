from turtle import Turtle

midline = Turtle(visible=False)


def draw_midline():
    midline.color("Yellow")
    midline.speed(0)
    midline.pu()
    midline.goto(x=0, y=-250)
    midline.setheading(90)
    midline.pensize(5)
    for i in range(25):
        midline.forward(20)
        if midline.isdown():
            midline.pu()
        else:
            midline.pd()