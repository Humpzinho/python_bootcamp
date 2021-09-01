from turtle import Turtle

SMALL_FONT = ("Nokia Cellphone FC", 12, "bold")
SCORE_FONT = ("Nokia Cellphone FC", 36, "bold")
BIG_FONT = ("Nokia Cellphone FC", 64, "bold")
GAME_OVER_FONT = ("Nokia Cellphone FC", 64, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=0, y=360)
        self.setheading(90)
        self.pensize(2.25)
        self.score_bot = 0
        self.score_p = 0
        self.p_enter = True
        self.p2_enter = True
        self.again = True

    def draw_line(self):
        self.goto(0, 360)
        self.setheading(90)
        for _ in range(40):
            self.penup()
            self.backward(13)
            self.pendown()
            self.backward(13)
        self.penup()

    def text_update(self):
        self.clear()
        self.draw_line()
        if self.again == True:
            self.player_enter()
        self.setheading(0)
        self.goto(60, 280)
        self.write(self.score_bot, align="center", font=SCORE_FONT)
        self.setheading(0)
        self.goto(-60, 280)
        self.write(self.score_p, align="center", font=SCORE_FONT)
        
    def score_center(self):
        self.clear()
        self.again = False
        self.player_enter()
        self.draw_line()
        self.setheading(0)
        self.goto(90, -50)
        self.write(self.score_bot, align="center", font=BIG_FONT)
        self.goto(-90, -50)
        self.write(self.score_p, align="center", font=BIG_FONT)
        
    def player_enter(self):
        if self.again == True:
            self.again = False
            self.clear()
            self.text_update()
            self.draw_line()
        self.again = True
            
        if self.p2_enter == True:
            self.draw_line()
            self.setheading(0)
            self.goto(490, 332)
            self.write("Press ENTER to play.", align="center", font=SMALL_FONT)
            
        if self.p_enter == True:
            self.draw_line()
            self.setheading(0)
            self.goto(-490, 332)
            self.write("Press SPACE to play.", align="center", font=SMALL_FONT)
            
    def win_1(self):
        self.clear()
        self.setheading(0)
        self.again = False
        self.text_update()
        self.player_enter()
        self.goto(0, -95)
        self.write("Player 1\n   Wins", align="center", font=GAME_OVER_FONT)
        
    def win_2(self):
        self.clear()
        self.setheading(0)
        self.again = False
        self.text_update()
        self.player_enter()
        self.goto(0, -95)
        self.write("Player 2\n   Wins", align="center", font=GAME_OVER_FONT)
        

