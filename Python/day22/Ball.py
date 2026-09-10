from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        #x, y = position
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.goto(0,0)


    def move(self):
        #The ball has to move x,y like a diagonal
        self.goto(self.xcor()+.1,self.ycor()+.075)
        