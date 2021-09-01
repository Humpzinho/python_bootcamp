#IMPORTS
from scoreboard import Scoreboard
from turtle_crossing import Turtle_Cross
from turtle import Screen
from car import Car
import time
import random

#CONSTANTS
FPS = 30
TIME_FRAME = 1000 / FPS / 1000

#VARIABLES
car_list = []
game_on = True

#SCREEN SETTINGS
s = Screen()
s.colormode(255)
s.tracer(False)
s.setup(500, 500)

#TURTLE, CAR OBJECT/LIST, SCOREBOARD
t = Turtle_Cross()

for _ in range(20):
    c = Car()
    c.goto(random.randrange(200, 800, 20), random.randrange(-200, 200, 20))
    car_list.append(c)
    
sb = Scoreboard()
sb.update_score()

#KEYS LISTENING
s.onkeypress(fun=t.move, key="w")
s.onkeypress(fun=t.move_back, key="s")
s.listen()

#MAIN LOOP
while game_on:
    #SCREEN UPDATE
    s.update()
    time.sleep(TIME_FRAME)

    #LOOP THROUGH EACH CAR AND UPDATE CAR POSITION
    for car in car_list:
        car.move()
        if car.xcor() <= -280:
            car.goto(280, random.randrange(-200, 200, 20))

        #CHECK COLLISION WITH CAR
        if t.distance(car) < 20:
            t.goto(0, -230)
            sb.game_over()
            game_on = False

    #CHECK IF THE TURTLE ARRIVED AT THE END OF THE STREET
    if t.ycor() >= 230:
        t.goto(0, -230)
        for car in car_list:
            car.speed_car += 2.5
        sb.level += 1
        sb.update_score()
        
s.exitonclick()