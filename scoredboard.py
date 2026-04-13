from turtle import Turtle

class scoredboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highScore = self.get_highscore()
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.update_scoreboard()

    def get_highscore(self):
        with open("highScore.txt", "r") as file:
            return int(file.read())


    def update_scoreboard(self):
        self.write(f"Score: {self.score}  High Score: {self.highScore}", align='center', font=('Arial', 14, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        if self.score > self.highScore:
            self.highScore = self.score
            with open("highScore.txt", "w") as file:
                file.write(str(self.highScore))
        self.clear()
        self.screen.bgcolor("darkred")
        self.goto(0, -30)
        if self.highScore < self.score:
            self.highScore = self.score
        self.write(f"--- Game Over ---\n\n    Final Score: {self.score}\n\n    High Score: {self.highScore}", align='center', font=('Arial', 18, 'normal'))
