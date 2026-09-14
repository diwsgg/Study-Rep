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
        self.goto(STARTING_POSITION)

    def moveUp(self):
        newy = self.ycor()+10
        self.sety(newy)

    #Instead of checking on main, we are checking this if its true then we can continue
    def resetPosition(self):
        if self.ycor()>=FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True