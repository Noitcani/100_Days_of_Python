import turtle
from turtle import Turtle, Screen
import random

color = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

screen = Screen()
screen.setup(width=600, height=400)

turtle_list = []
turtle_starting_y = -150

user_bet = turtle.textinput(title="Place Your Bets!",
                 prompt='''
                 Enter the color you want to bet on: 
                 "red", "orange", "yellow", "green", "blue", "indigo", "violet")
                 ''')

race_on = True

starting_line = Turtle()
starting_line.ht()
starting_line.pu()
starting_line.setpos(x=250, y=-200)
starting_line.setheading(90)
starting_line.pensize(5)
starting_line.pd()
starting_line.forward(400)


for i in color:
    new_turtle = Turtle(shape="turtle")
    new_turtle.fillcolor(i)
    new_turtle.pu()
    new_turtle.setpos(x=-280, y=turtle_starting_y)
    turtle_list.append(new_turtle)
    turtle_starting_y += 50

while race_on:
    for x in turtle_list:
        x.forward(random.randint(0, 10))
        if x.xcor() > 230:
            race_on = False
            if user_bet == x.fillcolor():
                print(f"You win! The {x.fillcolor()} turtle was first!")
            else:
                print(f"You lose! The {x.fillcolor()} turtle was first!")

screen.exitonclick()

