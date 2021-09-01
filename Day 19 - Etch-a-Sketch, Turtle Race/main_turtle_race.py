from random import randint
from turtle import Turtle, Screen

is_on = True
s = Screen()
s.setup(width=500, height=400)
user_bet = s.textinput("Make your bet",
                       "Which turtle will win the race? Choose a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
ypos = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for index in range(0, 6):
    t = Turtle(shape="turtle")
    t.speed(2)
    t.color(colors[index])
    t.penup()
    t.goto(-230, ypos[index])
    all_turtles.append(t)

while is_on:
    for turtle in all_turtles:
        if turtle.xcor() >= 230:
            print(turtle.color())
            is_on = False
            if turtle.pencolor() == user_bet:
                print(
                    f"You got it right! The {turtle.pencolor()} turtle is the winner!"
                )
            else:
                print(
                    f"You got it wrong. The {turtle.pencolor()} turtle is the winner."
                )
            break

        turtle.forward(randint(1, 10))

s.exitonclick()