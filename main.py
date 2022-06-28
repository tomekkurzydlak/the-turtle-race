import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=800, height=500)
screen.title("The Turtle Race by Tomek")

color_list = ["pink", "black", "yellow", "blue", "red"]
steps = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
all_turtles = []
y_positions = [-100, -50, 0, 50, 100]
wallet = 0
bets = [1, 1.25, 1.5, 1.75, 2, 2.5, 3, 3.5]
bets_picked = []

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
    bet_value = random.choice(bets)
    bets_picked.append(bet_value)

worker.penup()
worker.goto(-280, 120)
worker.pendown()
worker.goto(-280, -120)
worker.penup()
worker.goto(270, 120)
worker.pendown()
worker.goto(270, -120)
worker.hideturtle()
worker.penup()
worker.goto(-85, 150)
worker.color("BLACK")
worker.write("THE TURTLE RACE", font=('Courier', 18, 'normal'))

bet_on = turtle.textinput("Bet on your turtle!", f"Pick color: pink: 1:{bets_picked[0]}, black: 1:{bets_picked[1]}, "
                                                 f"yellow: 1:{bets_picked[2]}, blue: 1:{bets_picked[3]} "
                                                 f"or red: 1:{bets_picked[4]}\n")
dollars = int(turtle.textinput(f"You bet on {bet_on}!", f"How much you bet on {bet_on}? "
                                                    f"We pay 1:{bets_picked[color_list.index(bet_on.lower())]}"))

on_position = False

def steps_picker():
    return random.choice(steps)

def if_on_position(any_turtle):
    global wallet
    if any_turtle.xcor() >= 251:
        worker.penup()
        worker.goto(-250, y_positions[color_list.index(bet_on.lower())] - 10)
        worker.write(f"YOU BET ON {bet_on.upper()}==>", font=('Courier', 18, 'normal'))
        worker.goto(-10, y_positions[color_list.index(any_turtle.pencolor())]-10)
        worker.write(f"{any_turtle.pencolor().upper()} IS THE WINNER==>", font=('Courier', 18, 'normal'))
        if bet_on.lower() == any_turtle.pencolor():
            print(f"{any_turtle.pencolor().capitalize()} win the race. You bet on {bet_on}\nYou win")
            wallet += dollars * bets_picked[color_list.index(bet_on.lower())]
            worker.penup()
            worker.goto(-85, -150)
            worker.write("CONGRATULATIONS!", font=('Courier', 18, 'normal'))
            worker.goto(-60, -170)
            worker.pencolor("green")
            worker.write(f"YOUR WALLET: ${wallet}", font=('Courier', 13, 'normal'))
        else:
            print(f"{any_turtle.pencolor().capitalize()} win the race. You bet on {bet_on}\nYou lose")
            wallet -= dollars
            worker.penup()
            worker.goto(-45, -150)
            worker.write("YOU LOSE!", font=('Courier', 18, 'normal'))
            worker.goto(-60, -170)
            worker.pencolor("red")
            worker.write(f"YOUR WALLET: ${wallet}", font=('Courier', 13, 'normal'))
        return True

while not on_position:
    for turtle in all_turtles:
        turtle.forward(steps_picker())
        if if_on_position(turtle):
            on_position = True



screen.exitonclick()