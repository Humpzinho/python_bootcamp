from turtle import Turtle, Screen
import time

INIT_COUNT_SEGMENTS = 4
MOVE_DISTANCE = 20


class Snake():
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]
        self.head_style()

    def create_snake(self):
        for x in range(INIT_COUNT_SEGMENTS):
            self.add_segment(x)

    def add_segment(self, x):
        x -= 1
        t = Turtle(shape="square", )
        t.penup()
        t.color((255, 200, 0))
        t.shapesize(0.8)
        self.snake_segments.append(t)
        if x != 0: t.goto(self.snake_segments[x].pos())
        t.backward(MOVE_DISTANCE)

    def color_tail(self):
        for segment in self.snake_segments[1:]:
            if self.snake_segments.index(segment) % 5 == 0:
                segment.color((255, 255, 60))
            else:
                segment.color((255, 200, 0))

    def pass_food(self):
        for segment in self.snake_segments[1:]:
            segment.color((255, 99, 71))

    def collided(self):
        for segment in self.snake_segments[1:]:
            segment.color((255, 70, 40))

    def extends(self):
        self.add_segment(-1)
        self.color_tail()

    def head_style(self):
        self.head.shape("triangle")
        self.head.color((255, 99, 71))

    def move(self):
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            x = self.snake_segments[seg_num - 1].xcor()
            y = self.snake_segments[seg_num - 1].ycor()
            self.snake_segments[seg_num].goto(x, y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)