from turtle import Turtle, Screen, mode


FONT = ('Arial', 24, 'normal')
ALIGNMENT = "center"

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()

        with open("high_score_data.txt") as file:
            self.high_score = int(file.read())
        
        self.score = 0
        self.penup()
        self.goto(0,260)
        self.color("white")
        self.hideturtle()
        self.show_scoreboard()

    def show_scoreboard(self):
        self.clear()
        self.check_highscore()
        self.goto(0,260)
        self.write(f"Score = {self.score} High Score = {self.high_score}", True,  align = ALIGNMENT, font = FONT)

    def score_increased(self):
        self.score += 1
        self.show_scoreboard()

    def check_highscore(self):
        if self.high_score < self.score:
            self.high_score = self.score
            with open("high_score_data.txt", mode = "w") as file:
                file.write(f"{self.high_score}")


    def reset(self):
        self.check_highscore()
        self.score = 0
        self.show_scoreboard()

    # def game_over(self):
        # self.goto(0,0)
        # self.write("Game Over", True,  align = ALIGNMENT, font = FONT)
    
