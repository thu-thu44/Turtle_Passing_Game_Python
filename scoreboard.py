from turtle import Turtle
FONT = ("Arial",30,"normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.level = 1
        self.speed = 0.1
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-380,240)
        self.write(f"LEVEL :{self.level}",align="left",font=FONT)

    def update_level(self):
        self.level += 1
        self.speed *= 0.4
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.penup()
        self.write(f"GAME OVER",align="center",font=FONT)




    

    

