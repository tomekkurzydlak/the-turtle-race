import turtle
from turtle import Turtle, Screen
import random

color_list = ["red", "yellow", "pink", "black", "blue"]
steps = [0, 1, 2, 3, 4, 5, 6]
all_turtles = []
y_positions = [-100, -50, 0, 50, 100]

worker = Turtle()
worker.speed(7)
worker.hideturtle()
worker.color("grey")

for turtle_nr in range(0, 5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color_list[turtle_nr])
    new_turtle.goto(x=-300, y=y_positions[turtle_nr])
    all_turtles.append(new_turtle)


worker.penup()
worker.goto(-280, 120)
worker.pendown()
worker.goto(-280, -120)
worker.penup()
worker.goto(270, 120)
worker.pendown()
worker.goto(270, -120)
worker.hideturtle()

bet_on = turtle.textinput("Bet on your turtle!", "Pick color: red, yellow, blue, black or pink")

win_color = ""

def steps_picker():
    return random.choice(steps)

def if_on_position(any_turtle):
    global win_color
    if any_turtle.xcor() >= 251:
        win_color = any_turtle.pencolor()
        return any_turtle.color()

on_position = False

while not on_position:

    for turtle in all_turtles:
        if if_on_position(turtle):
            on_position = True
        turtle.forward(steps_picker())

print(win_color)

if bet_on.lower() == win_color:
    print("You win")
else:
    print("You lose")

screen = Screen()
screen.setup(width=600, height=400)

screen.exitonclick()