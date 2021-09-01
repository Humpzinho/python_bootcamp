from turtle import Turtle, Screen
import random

t = Turtle()
s = Screen()
s.colormode(255)
s.tracer(False)

rgb_colors = [(58, 106, 148), (224, 200, 110), (134, 84, 58), (223, 138, 62), (196, 145, 171), (142, 178, 203), (139, 82, 105), (208, 90, 69), (188, 80, 120), (69, 105, 90), (133, 182, 135), (133, 133, 74), (64, 156, 92), (47, 156, 193), (183, 192, 201), (213, 177, 191), (19, 58, 92), (20, 68, 113), (113, 123, 149), (227, 174, 166), (172, 203, 183), (156, 206, 217), (69, 58, 47), (72, 64, 53), (111, 46, 59), (53, 70, 64)]

#there some problems here... just put 100
dot_count_input = int(s.textinput("Dot count.", "How many dots do you want?\n:"))
dot_count = int(str(dot_count_input // 4) + "0")

while True:
    s.reset()
    t.hideturtle()
    t.penup()
    for y in range(-dot_count, dot_count, 50):
        for x in range(-dot_count, dot_count, 50):
            t.goto(x, y)
            t.dot(20, random.choice(rgb_colors))
    s.update()        
