from turtle import Turtle

PADDLE_SIZE_LEN = 5
PADDLE_SIZE_WID = 0.8

class Paddle(Turtle):
    def __init__(self, player):
        super().__init__()
        self.MOVE_BOT_SPEED = 15
        self.MOVE_SPEED = 15
        self.moving = "down"
        self.shape("square")
        self.color("white")
        self.penup()
        self.player = player
        self.setheading(270)
        self.player_add = False
        self.shapesize(stretch_len=PADDLE_SIZE_LEN, stretch_wid=PADDLE_SIZE_WID)
        if player == 1:
            self.goto(x=-620, y=0)
        else:
            self.goto(x= 610, y=0)

    def move_up(self):
        if self.player == 1:
            if self.ycor() < 290:
                self.backward(self.MOVE_SPEED)
        else:
            if self.ycor() < 290:
                self.backward(self.MOVE_BOT_SPEED)

    def move_down(self):
        if self.player == 1:
            if self.ycor() > -285:
                self.forward(self.MOVE_SPEED)
        else:
            if self.ycor() > -285:
                self.forward(self.MOVE_BOT_SPEED)
            
    def player_enter(self):
        self.player_add = True