from turtle import Turtle

#CONSTANT
FONT = ("Nokia Cellphone FC", 14, "bold")
BIG_FONT = ("Nokia Cellphone FC", 32, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-185, 200)
        self.color("black")
        self.level = 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write("Level: " + str(self.level), align="center", font=FONT)
        
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=BIG_FONT)