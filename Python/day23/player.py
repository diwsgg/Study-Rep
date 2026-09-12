from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.teleport(0,-280)

    def moveUp(self):
        newy = self.ycor()+10
        self.sety(newy)

    def resetPosition(self):
        self.teleport(0,-280)