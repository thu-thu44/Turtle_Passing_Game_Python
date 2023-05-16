from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.color("black")
        self.penup()
        self.goto(0,-270)
        self.setheading(90)

    def move(self):
        self.forward(10)


    def start_again(self):
        self.goto(0,-270)

    

