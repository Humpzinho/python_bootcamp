from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
from just_playback import Playback

#RESOLVE AFTER:
#use undo method to the (down-left bug).
#high score.
#increase the speed.
s = Screen()


def screen_fun():
    s.setup(width=600, height=600)
    s.colormode(255)
    s.tracer(0)
    s.title("Snake Game")
    s.bgpic("Day 20 and 21 - Snake Game\extras\_bg_init.png")
    s.update()
    time.sleep(2)
    s.bgpic("nopic")


FPS = 15  #This define the fps and the velocity of snake
time_frame = 1000 / FPS / 1000  #Time between each frame (in miliseconds)

screen_fun()


def clear_all():
    print("CLEANING GAME")
    s.clear()
    main(time_frame, FPS)


playback = Playback()
playback.load_file('Day 20 and 21 - Snake Game\extras\_background_music.mp3')
playback.play()
playback.set_volume(0.1)


def main(time_frame, FPS):
    s.setup(width=600, height=600)
    s.colormode(255)
    s.title("Snake Game")
    s.tracer(0)
    s.bgcolor((0, 11, 13))

    snake = Snake()
    food = Food()
    sb = Scoreboard()

    def dead_animation():
        time.sleep(0.1)
        snake.collided()
        s.update()
        time.sleep(0.2)
        snake.color_tail()
        s.update()

    s.listen()
    s.onkey(snake.up, "w")
    s.onkey(snake.down, "s")
    s.onkey(snake.left, "a")
    s.onkey(snake.right, "d")
    game_over = False

    def check_food_position():
        stop = False
        while not stop:
            for segment in snake.snake_segments:
                if food.distance(segment.xcor(), segment.ycor()) < 5:
                    food.refresh_c()
                else:
                    stop = True
                    break

    while not game_over:
        check_food_position()
        if playback.active == False:
            playback.load_file('Day 20 and 21 - Snake Game\extras\_background_music.mp3')
            playback.play()
        snake.move()
        s.update()
        time.sleep(time_frame)

        #detect collision with food
        if snake.head.distance(food) < 5:
            snake.extends()
            food.refresh_c()
            sb.update_score()
            FPS += 0.1

        #detect collision with walls
        if round(snake.head.xcor()) > 295:
            snake.head.setx(round(-snake.head.xcor()))
        elif round(snake.head.xcor()) < -290:
            snake.head.setx(round(abs(snake.head.xcor())))
        elif round(snake.head.ycor()) > 295:
            snake.head.sety(round(-snake.head.ycor()))
        elif round(snake.head.ycor()) < -290:
            snake.head.sety(round(abs(snake.head.ycor())))

        #detect collision with tail
        for segment in snake.snake_segments[1:]:
            if snake.head.distance(segment) < 10:
                sb.game_over()
                for _ in range(5):
                    dead_animation()
                sb.game_over()
                s.onkey(clear_all, "space")
                s.exitonclick()


main(time_frame, FPS)
