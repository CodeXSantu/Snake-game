from turtle import Turtle
FONT = ("Courier",22,"normal")
MOVE = False
ALIGNMENT = "center" 

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.penup()
        self.goto(0,270)
        self.color("white")
        self.ht()
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score:{self.score} HIGH SCORE : {self.highscore}",move=MOVE,align=ALIGNMENT,font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt",mode="w") as data:
                data.write(f"{self.highscore}")

        self.score = 0
        self.update()


        
    def new_score(self):
        self.score +=1
        self.update()




