from turtle import Turtle, Screen
import pandas as pd
import time

SMALL_FONT = ("Arial", 7, "")
correct = 0
correct_list = []
s = Screen()
t = Turtle()
t.hideturtle()
t.penup()
s.title("U.S. States Game")
s.bgpic("Day 25 - U.S State Game\\blank_states_img.gif")
s.setup(width=700, height=500)

states_data = pd.read_csv("Day 25 - U.S State Game\\50_states.csv")
states_name = states_data["state"]
game_on = True

while game_on:

    anwser_state = s.textinput(
        str(correct) + "/50 Correct Anwsers",
        "What's another state name?: ").title()

    if anwser_state == "Exit":
        missing_state = pd.DataFrame([state for state in states_name if state not in correct_list]).to_csv("Day 25 - U.S State Game\\missing_state.csv")
        game_on = False

    for name in states_name:
        if name == anwser_state and name not in correct_list:
            print("OK")
            states_cord = states_data[states_data["state"] == name]
            x = states_cord["x"].to_list()
            y = states_cord["y"].to_list()
            t.goto(x[0], y[0])
            t.write(name, align="center", font=SMALL_FONT)
            correct_list.append(name)
            correct += 1
            break
        if correct == 50:
            game_on = False
