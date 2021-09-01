from turtle import Turtle

ALIGNMENT = "center"
SCORE_FONT = ("Nokia Cellphone FC", 16, "bold")
GAME_OVER_FONT = ("Nokia Cellphone FC", 34, "bold")
AGAIN_FONT = ("Nokia Cellphone FC", 11, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1

        with open("Day 20 and 21 - Snake Game\high_score.txt",
                  mode="r") as file:
            self.highscore = int(file.read())

        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.score += 1
        self.clear()

        if self.score > self.highscore:
            with open("Day 20 and 21 - Snake Game\high_score.txt",
                      mode="w") as file:
                file.write(str(self.score))
            self.highscore = self.score

        self.write(
            f"Score: {self.score}                          Highscore: {self.highscore}",
            align=ALIGNMENT,
            font=SCORE_FONT)

    def game_over(self):
        self.home()
        self.write(f"GAME OVER", align=ALIGNMENT, font=GAME_OVER_FONT)
        self.goto(0, -25)
        self.write(f"Press SPACE to play again.",
                   align=ALIGNMENT,
                   font=AGAIN_FONT)
        self.goto(0, -50)
        self.write(f"Press MOUSE1 to exit.", align=ALIGNMENT, font=AGAIN_FONT)
