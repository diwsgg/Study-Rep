COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = .05
MOVE_INCREMENT = 10
from turtle import Turtle
import random

class CarManager:
    def __init__(self):
        #Position of each one at x=280 (right), but "y" a random one between (-280,280)
        Yposition = random.randrange(-280,280)
        self.all_shapes = []
        self.createATurtle(Yposition)

    
    def createATurtle(self, Yposs):
        turtle = Turtle()
        turtle.penup()
        turtle.color(random.choice(COLORS))
        turtle.shape("square")
        turtle.shapesize(stretch_wid=1,stretch_len=2)
        turtle.goto(250, Yposs)
        self.all_shapes.append(turtle)

    def NewTurtle(self):
        Yposition = random.randrange(-280,280)
        self.createATurtle(Yposition)

    def Movement(self):
        a = STARTING_MOVE_DISTANCE
        #Moving only for x
        for t in range(len(self.all_shapes)):
            Xposition = self.all_shapes[t].xcor()
            self.all_shapes[t].setx(Xposition-a)



     