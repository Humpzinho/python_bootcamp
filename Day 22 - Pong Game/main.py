from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
import random
from just_playback import Playback

s = Screen()
playback = Playback()
playback2 = Playback()
playback.load_file('Day 22 - Pong Game\Extras\_music.mp3')
playback2.load_file('Day 22 - Pong Game\Extras\_pong.ogg')
playback.play()
playback.set_volume(0.2)


def screen_setup():
    s.tracer(False)
    s.setup(width=1280, height=720)
    s.title("Pong Game")
    s.bgcolor("black")


screen_setup()


def reset_all():
    s.reset()
    screen_setup()
    main(TIME_FRAME)


FPS = 45
TIME_FRAME = 1000 / FPS / 1000
WALL_CORDS = 330
DISTANCE_COLLISION = 70

sb = Scoreboard()
paddle = Paddle(1)
paddle_1 = Paddle(2)
ball = Ball()


def main(TIME_FRAME):
    sb.text_update()

    #KEYS
    s.onkeypress(fun=paddle.move_up, key="w")
    s.onkeypress(fun=paddle.move_down, key="s")
    s.onkeypress(fun=paddle.player_enter, key="space")
    s.onkeypress(fun=paddle_1.move_up, key="Up")
    s.onkeypress(fun=paddle_1.move_down, key="Down")
    s.onkeypress(fun=paddle_1.player_enter, key="Return")

    s.listen()
    again = True
    again2 = True
    collided = 3
    #MAIN LOOP
    while True:
        if sb.score_p == 10:
            ball.hideturtle()
            s.update()
            sb.win_1()
            sb.score_bot = 0
            sb.score_p = 0
            time.sleep(4)
            ball.showturtle()
            sb.score_center()
        if sb.score_bot == 10:
            ball.hideturtle()
            s.update()
            sb.win_2()
            sb.score_bot = 0
            sb.score_p = 0
            time.sleep(4)
            ball.showturtle()
            sb.score_center()

        if playback.active == False:
            playback.load_file('Day 22 - Pong Game\Extras\_music.mp3')
            playback.play()

        if ball.game_over == True:
            ball.goto(0, random.randint(-250, 250))
            sb.text_update()
            ball.BALL_SPEED = 15
            ball.game_over = False

        #PLAYER 1 or bot
        if paddle.player_add == False:
            if ball.ycor() > -290 and ball.ycor() < 290:
                if ball.xcor() < -30:
                    if ball.ycor() > paddle.ycor() + 25:
                        paddle.move_up()
                    elif ball.ycor() < paddle.ycor() - 25:
                        paddle.move_down()
        else:
            if again == True:
                sb.p_enter = False
                paddle.MOVE_SPEED = 40
                sb.text_update()
                again = False

        #BOT OR PLAYER 2 MOVE
        if paddle_1.player_add == False:
            if ball.ycor() > -290 and ball.ycor() < 290:
                if ball.xcor() > 30:
                    if ball.ycor() > paddle_1.ycor() + 25:
                        paddle_1.move_up()
                    elif ball.ycor() < paddle_1.ycor() - 25:
                        paddle_1.move_down()
        else:
            if again2 == True:
                sb.p2_enter = False
                paddle_1.MOVE_BOT_SPEED = 40
                sb.text_update()
                again2 = False

        #LEFT
        if ball.xcor() < -610:
            ball.game_over = True
            ball.setheading(random.choice((135, 224)))
            sb.score_bot += 1
            ball.hideturtle()
            sb.score_center()
            s.update()
            time.sleep(2)
            ball.showturtle()
            ball.move()

        #RIGHT
        if ball.xcor() > 610:
            ball.game_over = True
            ball.setheading(random.choice((45, 314)))
            sb.score_p += 1
            ball.hideturtle()
            sb.score_center()
            s.update()
            time.sleep(2)
            ball.showturtle()
            ball.move()

        #PADDLE 1 COLLISION
        if ball.distance(paddle) < DISTANCE_COLLISION and ball.xcor(
        ) < -590 and collided != 0:
            print(ball.distance(paddle))
            if ball.heading() > 90 and ball.heading() < 180:
                #45
                ball.setheading(0 + abs(ball.distance(paddle)))
            elif ball.heading() >= 180 and ball.heading() < 270:
                #315
                ball.setheading(360 - abs(ball.distance(paddle)))
            playback2.load_file('Day 22 - Pong Game\Extras\_pong.ogg')
            playback2.play()
            ball.BALL_SPEED = random.randrange(
                15, 30) + (ball.distance(paddle) // 10)
            collided = 0

        #PADDLE 2 COLLISION
        if ball.distance(paddle_1) < DISTANCE_COLLISION and ball.xcor(
        ) > 585 and collided != 1:
            print(ball.distance(paddle_1))
            if ball.heading() >= 270:
                #225
                ball.setheading(180 + abs(ball.distance(paddle_1)))
            elif ball.heading() <= 90:
                #135
                ball.setheading(90 + abs(ball.distance(paddle_1)))
            playback2.load_file('Day 22 - Pong Game\Extras\_pong.ogg')
            playback2.play()
            ball.BALL_SPEED = random.randrange(
                15, 30) + (ball.distance(paddle_1) // 10)
            collided = 1

        #UP
        if ball.ycor() > WALL_CORDS + 5:
            if ball.heading() <= 90:
                ball.setheading(315)
            elif ball.heading() > 90 and ball.heading() < 180:
                ball.setheading(225)

        #DOWN
        if ball.ycor() < -WALL_CORDS - 7:
            if ball.heading() >= 270:
                ball.setheading(45)
            elif ball.heading() >= 180 and ball.heading() < 270:
                ball.setheading(135)

        ball.move()
        s.update()
        time.sleep(TIME_FRAME)


main(TIME_FRAME)