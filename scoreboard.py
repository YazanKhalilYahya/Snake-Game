from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", "r") as file:
            first_line = int(file.readline(1))
        self.high_score = first_line
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}",True, align="center", font=("Arial", 14, "normal"))
        self.goto(0,270)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("data.txt", "a") as file:
            file.writelines(f"\n{self.high_score}")

        # reset the score
        self.score = 0

        # update the scoreboard
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

