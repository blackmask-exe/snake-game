from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("highscore.txt") as highscore_data:
            self.highscore = highscore_data.read()
        self.color("white")
        self.speed("fastest")
        self.score = 0

    def update_score(self):
        self.clear()
        self.write(f"SCORE: {self.score}, High Score: {self.highscore}", False, "center", ('Arial', 16, 'normal'))

    def reset(self):
        if int(self.score) > int(self.highscore):
            with open("highscore.txt", mode="w") as highscore_data:
                self.highscore = self.score
                highscore_data.write(str(self.highscore))

        self.score = 0
        self.update_score()

    def scoreboard_display(self):
        self.teleport(0, 260)
        self.hideturtle()
        self.update_score()

    def game_over(self):
        self.teleport(0, 0)
        self.write("GAME OVER", False, "center", ('Arial', 25, 'normal'))
        self.hideturtle()
